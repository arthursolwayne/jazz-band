
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2 (1.5 - 3.0s)
# Sax melody
sax_notes = [
    # D (D4) - start
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    # F# (F#4) - chromatic approach
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),
    # B (B4) - tension
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),
    # D (D4) - resolve
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),
    # F# (F#4) - hanging
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.75),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line (walking)
bass_notes = [
    # D (D3)
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),
    # E (E3)
    pretty_midi.Note(velocity=80, pitch=52, start=1.75, end=2.0),
    # F# (F#3)
    pretty_midi.Note(velocity=80, pitch=53, start=2.0, end=2.25),
    # G (G3)
    pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.5),
    # A (A3)
    pretty_midi.Note(velocity=80, pitch=57, start=2.5, end=2.75),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano chords (7th chords, comp on 2 and 4)
piano_notes = [
    # D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=74, start=1.75, end=2.0),
    # D7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=74, start=2.75, end=3.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3 (3.0 - 4.5s)
# Sax melody (continue)
sax_notes = [
    # D (D4) - return
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
    # F# (F#4) - tension
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),
    # B (B4) - tension
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),
    # D (D4) - resolve
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),
    # F# (F#4)
    pretty_midi.Note(velocity=100, pitch=66, start=4.0, end=4.25),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line (walking)
bass_notes = [
    # B (B3)
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),
    # C# (C#4)
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.5),
    # D (D4)
    pretty_midi.Note(velocity=80, pitch=72, start=3.5, end=3.75),
    # E (E4)
    pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=4.0),
    # F# (F#4)
    pretty_midi.Note(velocity=80, pitch=77, start=4.0, end=4.25),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano chords (7th chords, comp on 2 and 4)
piano_notes = [
    # D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.5),
    # D7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=71, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=74, start=4.25, end=4.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4 (4.5 - 6.0s)
# Sax melody (finish)
sax_notes = [
    # D (D4) - finish
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),
    # F# (F#4) - hanging
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),
    # B (B4) - hanging
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),
    # D (D4) - finish
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),
    # F# (F#4) - hanging
    pretty_midi.Note(velocity=100, pitch=66, start=5.5, end=5.75),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line (walking)
bass_notes = [
    # G (G3)
    pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=4.75),
    # A (A3)
    pretty_midi.Note(velocity=80, pitch=57, start=4.75, end=5.0),
    # B (B3)
    pretty_midi.Note(velocity=80, pitch=59, start=5.0, end=5.25),
    # C# (C#4)
    pretty_midi.Note(velocity=80, pitch=61, start=5.25, end=5.5),
    # D (D4)
    pretty_midi.Note(velocity=80, pitch=62, start=5.5, end=5.75),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano chords (7th chords, comp on 2 and 4)
piano_notes = [
    # D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=74, start=4.75, end=5.0),
    # D7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=5.75, end=6.0),
    pretty_midi.Note(velocity=90, pitch=67, start=5.75, end=6.0),
    pretty_midi.Note(velocity=90, pitch=71, start=5.75, end=6.0),
    pretty_midi.Note(velocity=90, pitch=74, start=5.75, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=38, start=2.0, end=2.375),
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=38, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
