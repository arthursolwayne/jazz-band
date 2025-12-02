
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
drum_pattern = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_pattern)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass - walking line in Fm
bass_line = [
    # Fm7 chord: F, Ab, Bb, D
    # Chromatic approach to F
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # F
    # Chromatic approach to Ab
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=3.0), # Ab
    # Chromatic approach to Bb
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375), # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75), # Bb
    # Chromatic approach to D
    pretty_midi.Note(velocity=100, pitch=73, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5), # D
    # Chromatic approach to F again
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875), # Eb
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25), # F
    # Chromatic approach to Ab
    pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=80, start=5.625, end=6.0), # Ab
]
bass.notes.extend(bass_line)

# Diane on piano - 7th chords on 2 and 4
# Fm7: F, Ab, Bb, D (Fm7)
# Bb7: Bb, D, F, Ab (Bb7)
# Eb7: Eb, G, Bb, D (Eb7)
# Ab7: Ab, C, Eb, G (Ab7)
piano_notes = [
    # Bar 2, beat 2: Fm7
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625), # D
    # Bar 2, beat 4: Bb7
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375), # Ab
    # Bar 3, beat 2: Eb7
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125), # D
    # Bar 3, beat 4: Ab7
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.875), # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875), # G
    # Bar 4, beat 2: Fm7
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.625), # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625), # D
    # Bar 4, beat 4: Empty
]
piano.notes.extend(piano_notes)

# Dante on sax - short motif that sings, starts, leaves it hanging, comes back and finishes
# Fm - F, Ab, Bb, D
# Motif: F, Bb, Ab, F
sax_notes = [
    # Bar 2, beat 1: F
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.875),
    # Bar 2, beat 2: Bb
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625),
    # Bar 2, beat 3: Ab
    pretty_midi.Note(velocity=110, pitch=68, start=3.0, end=3.375),
    # Bar 2, beat 4: F
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125),
    # Bar 3, beat 1: F (repeat)
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),
    # Bar 3, beat 2: Bb
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.625),
    # Bar 3, beat 3: Ab
    pretty_midi.Note(velocity=110, pitch=68, start=5.625, end=6.0)
]
sax.notes.extend(sax_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file to a file
midi.write("dante_intro.mid")
