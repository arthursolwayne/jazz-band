
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
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.75),  # D2 (Fm root)
    pretty_midi.Note(velocity=90, pitch=41, start=1.75, end=2.0),  # F#2 (chromatic approach to G2)
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.25),  # G2 (Fm fifth)
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.5),  # E2 (chromatic approach to D2)
    pretty_midi.Note(velocity=90, pitch=38, start=2.5, end=2.75),  # D2 (Fm root)
    pretty_midi.Note(velocity=90, pitch=41, start=2.75, end=3.0),  # F#2 (chromatic approach to G2)
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=3.0),  # Ab4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),  # C5
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),  # D5
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Motif starts on bar 2, one short phrase, sings, leaves it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # C5
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # Ab4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.25),  # G2 (Fm fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=3.25, end=3.5),  # F#2 (chromatic approach to G2)
    pretty_midi.Note(velocity=90, pitch=38, start=3.5, end=3.75),  # D2 (Fm root)
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.0),  # E2 (chromatic approach to D2)
    pretty_midi.Note(velocity=90, pitch=43, start=4.0, end=4.25),  # G2 (Fm fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=4.25, end=4.5),  # F#2 (chromatic approach to G2)
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Ab7 (Ab, C, Eb, G)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=4.5),  # Ab4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),  # C5
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=4.5),  # Eb5
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=4.5),  # G5
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Continue motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # Bb4
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # C5
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # Ab4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.75),  # D2 (Fm root)
    pretty_midi.Note(velocity=90, pitch=41, start=4.75, end=5.0),  # F#2 (chromatic approach to G2)
    pretty_midi.Note(velocity=90, pitch=43, start=5.0, end=5.25),  # G2 (Fm fifth)
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.5),  # E2 (chromatic approach to D2)
    pretty_midi.Note(velocity=90, pitch=38, start=5.5, end=5.75),  # D2 (Fm root)
    pretty_midi.Note(velocity=90, pitch=41, start=5.75, end=6.0),  # F#2 (chromatic approach to G2)
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=6.0),  # Bb4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0),  # D5
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=6.0),  # F5
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=6.0),  # Ab5
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # C5
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),  # Bb4
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.5),  # C5
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=66, start=5.75, end=6.0),  # C5
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))
    # Hihat on every eighth
    for eighth in range(0, 4):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + eighth * 0.375, end=start + eighth * 0.375 + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
