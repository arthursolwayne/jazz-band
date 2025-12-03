
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
bar_length = 1.5
for note in [36, 38, 42]:
    if note == 36:
        # Kick on 1 and 3
        times = [0.0, 0.75]
    elif note == 38:
        # Snare on 2 and 4
        times = [0.375, 1.125]
    else:
        # Hihat on every eighth
        times = [0.0, 0.375, 0.75, 1.125]
    for t in times:
        n = pretty_midi.Note(velocity=100, pitch=note, start=t, end=t + 0.125)
        drums.notes.append(n)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),  # D2
    pretty_midi.Note(velocity=80, pitch=53, start=1.75, end=2.0),  # F2
    pretty_midi.Note(velocity=80, pitch=51, start=2.0, end=2.25),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=57, start=2.25, end=2.5),  # A2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7
chord_notes = [50, 53, 57, 62]
for note in chord_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=1.5, end=3.0)
    piano.notes.append(n)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for note in [36, 38, 42]:
    if note == 36:
        times = [1.5, 2.25]
    elif note == 38:
        times = [1.875, 2.625]
    else:
        times = [1.5, 1.875, 2.25, 2.625]
    for t in times:
        n = pretty_midi.Note(velocity=100, pitch=note, start=t, end=t + 0.125)
        drums.notes.append(n)

# You: Saxophone, short motif, start it, leave it hanging
# Motif: Dm7 arpeggio with a chromatic twist
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),  # F4
    pretty_midi.Note(velocity=110, pitch=63, start=2.0, end=2.25),  # Eb4 (chromatic)
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),  # A4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.25),  # A2
    pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.5),  # C3
    pretty_midi.Note(velocity=80, pitch=58, start=3.5, end=3.75),  # Bb2 (chromatic)
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.0),  # D3
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Gm7
chord_notes = [55, 58, 62, 67]
for note in chord_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=3.0, end=4.5)
    piano.notes.append(n)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for note in [36, 38, 42]:
    if note == 36:
        times = [3.0, 3.75]
    elif note == 38:
        times = [3.375, 4.125]
    else:
        times = [3.0, 3.375, 3.75, 4.125]
    for t in times:
        n = pretty_midi.Note(velocity=100, pitch=note, start=t, end=t + 0.125)
        drums.notes.append(n)

# You: Saxophone, short motif, start it, leave it hanging
# Motif: Gm7 arpeggio with a chromatic twist
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=110, pitch=70, start=3.25, end=3.5),  # Bb4
    pretty_midi.Note(velocity=110, pitch=68, start=3.5, end=3.75),  # Ab4 (chromatic)
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.0),  # D5
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),  # D3
    pretty_midi.Note(velocity=80, pitch=65, start=4.75, end=5.0),  # F3
    pretty_midi.Note(velocity=80, pitch=63, start=5.0, end=5.25),  # Eb3 (chromatic)
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5),  # A3
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cm7
chord_notes = [52, 55, 59, 64]
for note in chord_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=4.5, end=6.0)
    piano.notes.append(n)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for note in [36, 38, 42]:
    if note == 36:
        times = [4.5, 5.25]
    elif note == 38:
        times = [4.875, 5.625]
    else:
        times = [4.5, 4.875, 5.25, 5.625]
    for t in times:
        n = pretty_midi.Note(velocity=100, pitch=note, start=t, end=t + 0.125)
        drums.notes.append(n)

# You: Saxophone, short motif, start it, leave it hanging
# Motif: Cm7 arpeggio with a chromatic twist
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.75),  # C4
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),  # E4
    pretty_midi.Note(velocity=110, pitch=65, start=5.0, end=5.25),  # D4 (chromatic)
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5),  # G4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
