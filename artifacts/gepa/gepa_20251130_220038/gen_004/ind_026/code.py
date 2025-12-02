
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=100, pitch=48, start=2.625, end=3.0), # F
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375), # Ab
    pretty_midi.Note(velocity=100, pitch=51, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=100, pitch=48, start=4.125, end=4.5), # F
    pretty_midi.Note(velocity=100, pitch=49, start=4.5, end=4.875), # Gb
    pretty_midi.Note(velocity=100, pitch=47, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=100, pitch=48, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0), # Ab
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5-2.25)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25), # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25), # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25), # G
    # Bar 3 (2.25-3.0)
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=3.0), # C#
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=3.0), # D#
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=3.0), # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0), # G
    # Bar 4 (3.0-3.75)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75), # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75), # G
    # Bar 4 (3.75-4.5)
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.5), # C#
    pretty_midi.Note(velocity=100, pitch=63, start=3.75, end=4.5), # D#
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.5), # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.5), # G
    # Bar 4 (4.5-5.25)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.25), # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25), # G
    # Bar 4 (5.25-6.0)
    pretty_midi.Note(velocity=100, pitch=61, start=5.25, end=6.0), # C#
    pretty_midi.Note(velocity=100, pitch=63, start=5.25, end=6.0), # D#
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=6.0), # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=6.0), # G
]
piano.notes.extend(piano_notes)

# Sax (Dante): short motif, start, leave it hanging, finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # E
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375), # E
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5), # E
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0), # C
]
sax.notes.extend(sax_notes)

# Final setup
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
