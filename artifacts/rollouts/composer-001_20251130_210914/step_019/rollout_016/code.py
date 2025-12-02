
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    # Bar 2: D - C# - B - C - D (chromatic approach to D)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D3
    pretty_midi.Note(velocity=90, pitch=61, start=1.625, end=1.75),  # C#3
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=1.875),  # B3
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0),  # C3
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.125),  # D3
]

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 chord (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # F#3
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # A3
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.75),  # C3
]

# Sax: motif (D - F# - B - D)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D3
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),  # F#3
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=1.875),  # B3
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # D3
]

# Add notes to instruments
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: D - C# - B - C - D again (repeat for consistency)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.125),  # D3
    pretty_midi.Note(velocity=90, pitch=61, start=3.125, end=3.25),  # C#3
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.375),  # B3
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.5),  # C3
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.625),  # D3
]

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # D3
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # F#3
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # A3
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.25),  # C3
]

# Sax: motif again, but leave it hanging (end on F#)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # D3
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.25),  # F#3
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.375),  # B3
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5),  # F#3
]

# Add notes to instruments
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line: D - C# - B - C - D again
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.625),  # D3
    pretty_midi.Note(velocity=90, pitch=61, start=4.625, end=4.75),  # C#3
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=4.875),  # B3
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.0),  # C3
    pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.125),  # D3
]

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # D3
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # F#3
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # A3
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.75),  # C3
]

# Sax: finish the motif (F# to D)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.625),  # F#3
    pretty_midi.Note(velocity=100, pitch=62, start=4.625, end=4.75),  # D3
]

# Add notes to instruments
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
