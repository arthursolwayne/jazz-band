
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus - Walking bass line in D (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25), # A2 on 2
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625), # G#2 on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # D2 on 4
]

for note in bass_notes:
    bass.notes.append(note)

# Diane - Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (G4, B4, D5, F#5)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=3.0),  # D5
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=3.0),  # F#5
]

for note in piano_notes:
    piano.notes.append(note)

# Dante - Tenor sax. One short motif, make it sing.
# Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G4 on 1
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # A4 on 2
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # G4 on 4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus - Walking bass line in D (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # A2 on 2
    pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.125), # G#2 on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # D2 on 4
]

for note in bass_notes:
    bass.notes.append(note)

# Diane - Open voicings, different chord each bar, resolve on the last
# Bar 3: G7 (B4, D5, G5, F#5)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=4.5),  # G5
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=4.5),  # F#5
]

for note in piano_notes:
    piano.notes.append(note)

# Dante - Tenor sax. One short motif, make it sing.
# Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A4 on 1
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # G4 on 2
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # A4 on 4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus - Walking bass line in D (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # A2 on 2
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625), # G#2 on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # D2 on 4
]

for note in bass_notes:
    bass.notes.append(note)

# Diane - Open voicings, different chord each bar, resolve on the last
# Bar 4: C7 (E4, G4, C5, B4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # C5
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # B4
]

for note in piano_notes:
    piano.notes.append(note)

# Dante - Tenor sax. One short motif, make it sing.
# Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4 on 1
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25), # A4 on 2
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # G4 on 4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
