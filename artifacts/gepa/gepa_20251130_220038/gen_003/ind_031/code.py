
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=2.625, end=3.0),   # E
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=51, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),   # G
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=54, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25),  # Db
    pretty_midi.Note(velocity=90, pitch=56, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0),   # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=95, pitch=61, start=1.5, end=1.875),  # Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=95, pitch=61, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=95, pitch=61, start=4.5, end=4.875),
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=95, pitch=69, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Sax: Motif in Fm, short and singing
sax_notes = [
    # Start motif on beat 1 of bar 2
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # G (return)
]
sax.notes.extend(sax_notes)

# Drums: Same pattern for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
