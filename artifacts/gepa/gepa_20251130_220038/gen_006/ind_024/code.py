
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# D major key (D, E, F#, G, A, B, C#)
# Bar 2 (1.5 - 3.0s)
# Diane - piano: Comp on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2, measure 2: D7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875), # G
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875), # B
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875), # C#
    # Bar 2, measure 4: D7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=2.875), # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.875), # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.875), # B
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=2.875), # C#
]
piano.notes.extend(piano_notes)

# Marcus - bass: Walking line, chromatic approaches
bass_notes = [
    # Bar 2: D - C# - B - A
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=61, start=1.625, end=1.75),
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=1.875),
    pretty_midi.Note(velocity=90, pitch=59, start=1.875, end=2.0),
    # Bar 3: G - F# - E - D
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=66, start=2.125, end=2.25),
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=62, start=2.375, end=2.5),
    # Bar 4: A - G - F# - E
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.625),
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=66, start=2.75, end=2.875),
    pretty_midi.Note(velocity=90, pitch=65, start=2.875, end=3.0)
]
bass.notes.extend(bass_notes)

# Dante - sax: Motif: D - F# - E - D (start at bar 2)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),   # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),   # F#
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),   # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),   # D
    # Repeat motif, half-value
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0),   # D
]
sax.notes.extend(sax_notes)

# Add more drum hits in bars 2-4
# Bar 2
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0), # Snare
])
# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.875), # Snare
])
# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5), # Snare
])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
