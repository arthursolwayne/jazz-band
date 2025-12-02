
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
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everyone in
# Bass: D2 (MIDI 38) on beat 1, F#2 (MIDI 41) on beat 2, A2 (MIDI 45) on beat 3, C#3 (MIDI 48) on beat 4
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=48, start=2.625, end=3.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # C#5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif - G5 (MIDI 83) on beat 1, A5 (MIDI 84) on beat 2 (sustained), B5 (MIDI 85) on beat 3, G5 (MIDI 83) on beat 4 (half note)
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=83, start=1.5, end=1.875),
    pretty_midi.Note(velocity=105, pitch=84, start=1.875, end=2.625),
    pretty_midi.Note(velocity=105, pitch=85, start=2.625, end=3.0),
    pretty_midi.Note(velocity=105, pitch=83, start=2.625, end=3.0),
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Piano - A7 (A-C#-E-G#)
piano_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # C#5
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # E5
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.375),  # G#5
]
for note in piano_notes:
    piano.notes.append(note)

# Bass: A2 (MIDI 45) on beat 1, B2 (MIDI 46) on beat 2, D3 (MIDI 49) on beat 3, F#3 (MIDI 52) on beat 4
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=49, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=52, start=4.125, end=4.5),
]
for note in bass_notes:
    bass.notes.append(note)

# Sax: Motif variation - A5 (MIDI 84) on beat 1, B5 (MIDI 85) on beat 2, C#6 (MIDI 86) on beat 3, A5 (MIDI 84) on beat 4
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=84, start=3.0, end=3.375),
    pretty_midi.Note(velocity=105, pitch=85, start=3.375, end=4.125),
    pretty_midi.Note(velocity=105, pitch=86, start=4.125, end=4.5),
    pretty_midi.Note(velocity=105, pitch=84, start=4.125, end=4.5),
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Piano - B7 (B-D#-F#-A#)
piano_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # D#5
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=4.875),  # F#5
    pretty_midi.Note(velocity=100, pitch=83, start=4.5, end=4.875),  # A#5
]
for note in piano_notes:
    piano.notes.append(note)

# Bass: B2 (MIDI 46) on beat 1, D3 (MIDI 49) on beat 2, F#3 (MIDI 52) on beat 3, A3 (MIDI 55) on beat 4
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=46, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=49, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=55, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Sax: Motif resolution - B5 (MIDI 85) on beat 1, C#6 (MIDI 86) on beat 2, D6 (MIDI 87) on beat 3, B5 (MIDI 85) on beat 4 (half note)
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=85, start=4.5, end=4.875),
    pretty_midi.Note(velocity=105, pitch=86, start=4.875, end=5.625),
    pretty_midi.Note(velocity=105, pitch=87, start=5.625, end=6.0),
    pretty_midi.Note(velocity=105, pitch=85, start=5.625, end=6.0),
]
for note in sax_notes:
    sax.notes.append(note)

# Drums in bar 3 and 4
# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # Hi-hat
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Hi-hat
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
