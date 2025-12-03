
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line (F2 - C3)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # A2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # C3
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0), # Bb2 (chromatic approach)
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on last beat
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0), # F4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0), # A4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0), # C5
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0), # E5
]
for note in piano_notes:
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),    # hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Dante: Motif on tenor sax (F, Bb, D, F)
# Bar 2: Start the motif
note1 = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875) # F4
note2 = pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25) # Bb4
note3 = pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625) # D4
note4 = pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0)  # F4
sax.notes.append(note1)
sax.notes.append(note2)
sax.notes.append(note3)
sax.notes.append(note4)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line (F2 - C3)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375), # F2
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75), # A2
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125), # C3
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5), # Bb2
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on last beat
# Bar 3: Bbmaj7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5), # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5), # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5), # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5), # Ab4
]
for note in piano_notes:
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Dante: Finish the motif, then leave it hanging
note5 = pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375) # F4
note6 = pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75) # Bb4
note7 = pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125) # D4
note8 = pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5)  # F4
sax.notes.append(note5)
sax.notes.append(note6)
sax.notes.append(note7)
sax.notes.append(note8)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line (F2 - C3)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875), # F2
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25), # A2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # C3
    pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=6.0), # Bb2
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on last beat
# Bar 4: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0), # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0), # F4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0), # A4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0), # C4
]
for note in piano_notes:
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Dante: End with a question, leave it hanging
note9 = pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875) # F4
note10 = pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25) # Bb4
note11 = pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625) # D4
note12 = pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0)  # F4
sax.notes.append(note9)
sax.notes.append(note10)
sax.notes.append(note11)
sax.notes.append(note12)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
