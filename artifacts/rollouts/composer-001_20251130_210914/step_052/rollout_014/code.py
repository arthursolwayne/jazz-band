
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=46, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),   # E
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=90, pitch=44, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=4.125, end=4.5),   # G
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=45, start=4.5, end=4.875),  # Gb
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=90, pitch=41, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (F7)
    pretty_midi.Note(velocity=95, pitch=44, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=95, pitch=49, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=95, pitch=50, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=95, pitch=53, start=1.875, end=2.25),  # D
    # Bar 2, beat 4 (F7)
    pretty_midi.Note(velocity=95, pitch=44, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=95, pitch=49, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=95, pitch=50, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=95, pitch=53, start=2.625, end=3.0),   # D
    # Bar 3, beat 2 (F7)
    pretty_midi.Note(velocity=95, pitch=44, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=95, pitch=49, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=95, pitch=50, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=95, pitch=53, start=3.375, end=3.75),  # D
    # Bar 3, beat 4 (F7)
    pretty_midi.Note(velocity=95, pitch=44, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=95, pitch=49, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=95, pitch=50, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=95, pitch=53, start=4.125, end=4.5),   # D
    # Bar 4, beat 2 (F7)
    pretty_midi.Note(velocity=95, pitch=44, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=95, pitch=49, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=95, pitch=50, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=95, pitch=53, start=4.875, end=5.25),  # D
    # Bar 4, beat 4 (F7)
    pretty_midi.Note(velocity=95, pitch=44, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=95, pitch=49, start=5.625, end=6.0),   # A
    pretty_midi.Note(velocity=95, pitch=50, start=5.625, end=6.0),   # Bb
    pretty_midi.Note(velocity=95, pitch=53, start=5.625, end=6.0),   # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2, beat 1 (F, 44)
    pretty_midi.Note(velocity=110, pitch=44, start=1.5, end=1.875),
    # Bar 2, beat 2 (Ab, 47)
    pretty_midi.Note(velocity=110, pitch=47, start=1.875, end=2.25),
    # Bar 2, beat 3 (D, 49)
    pretty_midi.Note(velocity=110, pitch=49, start=2.25, end=2.625),
    # Bar 2, beat 4 (F, 44)
    pretty_midi.Note(velocity=110, pitch=44, start=2.625, end=3.0),
    # Bar 3, beat 1 (F, 44)
    pretty_midi.Note(velocity=110, pitch=44, start=3.0, end=3.375),
    # Bar 3, beat 2 (Ab, 47)
    pretty_midi.Note(velocity=110, pitch=47, start=3.375, end=3.75),
    # Bar 3, beat 3 (D, 49)
    pretty_midi.Note(velocity=110, pitch=49, start=3.75, end=4.125),
    # Bar 3, beat 4 (F, 44)
    pretty_midi.Note(velocity=110, pitch=44, start=4.125, end=4.5),
    # Bar 4, beat 1 (F, 44)
    pretty_midi.Note(velocity=110, pitch=44, start=4.5, end=4.875),
    # Bar 4, beat 2 (Ab, 47)
    pretty_midi.Note(velocity=110, pitch=47, start=4.875, end=5.25),
    # Bar 4, beat 3 (D, 49)
    pretty_midi.Note(velocity=110, pitch=49, start=5.25, end=5.625),
    # Bar 4, beat 4 (F, 44)
    pretty_midi.Note(velocity=110, pitch=44, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")
