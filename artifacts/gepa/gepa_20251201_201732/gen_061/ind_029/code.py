
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    note = pretty_midi.Note(velocity=100, pitch=36, start=i*0.375, end=(i+1)*0.375)
    drums.notes.append(note)
    if i % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=38, start=i*0.375, end=(i+1)*0.375)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=42, start=i*0.375, end=(i+1)*0.375)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: Fm7 (F, Ab, D, C)
# F (38), Ab (40), D (43), C (40)
notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=40, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.5)
]
bass.notes.extend(notes)

# Bar 3: Bb7 (Bb, D, F, Ab)
# Bb (41), D (43), F (45), Ab (40)
notes = [
    pretty_midi.Note(velocity=100, pitch=41, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=43, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=40, start=3.25, end=3.5)
]
bass.notes.extend(notes)

# Bar 4: Eb7 (Eb, G, Bb, D)
# Eb (43), G (47), Bb (46), D (43)
notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=47, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=46, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=43, start=4.25, end=4.5)
]
bass.notes.extend(notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
# F (45), Ab (40), C (40), D (43)
notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=40, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=40, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.25)
]
piano.notes.extend(notes)

# Bar 3: Bb7 (Bb, D, F, Ab)
# Bb (41), D (43), F (45), Ab (40)
notes = [
    pretty_midi.Note(velocity=100, pitch=41, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=43, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=45, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.25)
]
piano.notes.extend(notes)

# Bar 4: Eb7 (Eb, G, Bb, D)
# Eb (43), G (47), Bb (46), D (43)
notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=47, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=46, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=43, start=4.0, end=4.25)
]
piano.notes.extend(notes)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Fm7, start with a short motif
notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25)
]
sax.notes.extend(notes)

# Bar 3: Bb7, leave it hanging
note = pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75)
sax.notes.append(note)

# Bar 4: Eb7, come back and finish it
notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25)
]
sax.notes.extend(notes)

# Drums continue for bars 2-4
for i in range(4):
    note = pretty_midi.Note(velocity=100, pitch=36, start=(1.5 + i*0.375), end=(1.5 + (i+1)*0.375))
    drums.notes.append(note)
    if i % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=38, start=(1.5 + i*0.375), end=(1.5 + (i+1)*0.375))
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=42, start=(1.5 + i*0.375), end=(1.5 + (i+1)*0.375))
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
