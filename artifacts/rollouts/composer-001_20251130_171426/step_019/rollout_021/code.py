
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Sax enters with motif (1.5 - 3.0s)
# Motif: D (D4) -> F# (F#4) -> B (B4) -> D (D5) -> rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),  # D5
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 2: Bass enters with walking line (1.5 - 3.0s)
# D (D3) -> E (E3) -> F# (F#3) -> G (G3) -> A (A3) -> B (B3) -> C# (C#4) -> D (D4)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=45, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=70, pitch=47, start=1.75, end=2.0),  # E3
    pretty_midi.Note(velocity=70, pitch=49, start=2.0, end=2.25),  # F#3
    pretty_midi.Note(velocity=70, pitch=50, start=2.25, end=2.5),  # G3
    pretty_midi.Note(velocity=70, pitch=52, start=2.5, end=2.75),  # A3
    pretty_midi.Note(velocity=70, pitch=55, start=2.75, end=3.0),  # B3
    pretty_midi.Note(velocity=70, pitch=57, start=3.0, end=3.25),  # C#4
    pretty_midi.Note(velocity=70, pitch=58, start=3.25, end=3.5),  # D4
]

for note in bass_notes:
    bass.notes.append(note)

# Bar 2: Piano enters with comping (1.5 - 3.0s)
# 7th chords: D7 (D4, F#4, A4, C#5) on beat 2
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=2.0),  # D4
    pretty_midi.Note(velocity=80, pitch=66, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=80, pitch=72, start=1.75, end=2.0),  # C#5
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Sax repeats motif, but higher (3.0 - 4.5s)
# Motif again, but starting at F# (F#4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.75),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.0),  # F#5
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Bass continues walking line (3.0 - 4.5s)
# D (D4) -> E (E4) -> F# (F#4) -> G (G4) -> A (A4) -> B (B4) -> C# (C#5) -> D (D5)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=58, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=70, pitch=60, start=3.25, end=3.5),  # E4
    pretty_midi.Note(velocity=70, pitch=62, start=3.5, end=3.75),  # F#4
    pretty_midi.Note(velocity=70, pitch=64, start=3.75, end=4.0),  # G4
    pretty_midi.Note(velocity=70, pitch=66, start=4.0, end=4.25),  # A4
    pretty_midi.Note(velocity=70, pitch=69, start=4.25, end=4.5),  # B4
    pretty_midi.Note(velocity=70, pitch=71, start=4.5, end=4.75),  # C#5
    pretty_midi.Note(velocity=70, pitch=72, start=4.75, end=5.0),  # D5
]

for note in bass_notes:
    bass.notes.append(note)

# Bar 3: Piano plays comping again (3.0 - 4.5s)
# 7th chords: F#7 (F#4, A4, C#5, E5) on beat 2
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=66, start=3.25, end=3.5),  # F#4
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.5),  # A4
    pretty_midi.Note(velocity=80, pitch=72, start=3.25, end=3.5),  # C#5
    pretty_midi.Note(velocity=80, pitch=74, start=3.25, end=3.5),  # E5
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Sax ends motif (4.5 - 6.0s)
# D (D4) -> F# (F#4) -> B (B4) -> D (D5) -> rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5),  # D5
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Bass continues walking line (4.5 - 6.0s)
# D (D5) -> E (E5) -> F# (F#5) -> G (G5) -> A (A5) -> B (B5) -> C# (C#6) -> D (D6)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=72, start=4.5, end=4.75),  # D5
    pretty_midi.Note(velocity=70, pitch=74, start=4.75, end=5.0),  # E5
    pretty_midi.Note(velocity=70, pitch=76, start=5.0, end=5.25),  # F#5
    pretty_midi.Note(velocity=70, pitch=77, start=5.25, end=5.5),  # G5
    pretty_midi.Note(velocity=70, pitch=79, start=5.5, end=5.75),  # A5
    pretty_midi.Note(velocity=70, pitch=82, start=5.75, end=6.0),  # B5
    pretty_midi.Note(velocity=70, pitch=84, start=6.0, end=6.25),  # C#6
    pretty_midi.Note(velocity=70, pitch=85, start=6.25, end=6.5),  # D6
]

for note in bass_notes:
    bass.notes.append(note)

# Bar 4: Piano plays comping again (4.5 - 6.0s)
# 7th chords: B7 (B4, D5, F#5, A5) on beat 2
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=4.75, end=5.0),  # B4
    pretty_midi.Note(velocity=80, pitch=72, start=4.75, end=5.0),  # D5
    pretty_midi.Note(velocity=80, pitch=76, start=4.75, end=5.0),  # F#5
    pretty_midi.Note(velocity=80, pitch=79, start=4.75, end=5.0),  # A5
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Drums continue (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_introduction.mid")
