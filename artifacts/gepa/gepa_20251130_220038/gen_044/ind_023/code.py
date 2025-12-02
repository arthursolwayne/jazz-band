
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on beat 0 and 2
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on beat 1 and 3
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hats on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    # Add to drum instrument
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=80, pitch=38, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=80, pitch=40, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375),  # Gb
    pretty_midi.Note(velocity=80, pitch=38, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5),  # Gb
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=80, pitch=41, start=5.25, end=5.625), # Gb
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # D
]
piano.notes.extend(piano_notes)

# Drums: same pattern as bar 1
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on beat 0 and 2
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on beat 1 and 3
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hats on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    # Add to drum instrument
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, C, Db
# Motif: F, Ab, Bb, C (F -> Ab -> Bb -> C)

# Bar 2: Start motif
sax_note1 = pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.875)  # F
sax_note2 = pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25)  # Ab
sax_note3 = pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625)  # Bb
sax_note4 = pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0)   # C

# Bar 3: Leave it hanging
sax_note5 = pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375)  # F

# Bar 4: Return and finish it
sax_note6 = pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75)  # Ab
sax_note7 = pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.125)  # Bb
sax_note8 = pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5)   # C

# Add to sax
sax.notes.extend([sax_note1, sax_note2, sax_note3, sax_note4, sax_note5, sax_note6, sax_note7, sax_note8])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
