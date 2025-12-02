
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
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
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),  # C
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),   # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875), # D7 (F#)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875), # D7 (A)
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875), # D7 (B)
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375), # D7 (F#)
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375), # D7 (A)
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375), # D7 (B)
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875), # D7 (F#)
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875), # D7 (A)
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875), # D7 (B)
]
piano.notes.extend(piano_notes)

# Sax: Melody
# Short motif: D (62), F# (67), B (71), leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # B
    # Repeat motif starting at bar 3 (slightly altered)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # F#
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125), # B
    # Repeat again in bar 4 with a slight variation
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # F#
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # B
]
sax.notes.extend(sax_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
