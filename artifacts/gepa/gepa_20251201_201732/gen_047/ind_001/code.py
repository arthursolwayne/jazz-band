
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
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.05)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: F7 (F, C, A, E), root (F) on beat 1, 3, 4

note = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + 0.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.0 + 0.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.5 + 0.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.0 + 0.25)
bass.notes.append(note)

# Bar 3: Bb7 (Bb, F, D, A), root (Bb) on beat 1, 3, 4

note = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.0 + 0.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.5 + 0.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.0 + 0.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.5 + 0.25)
bass.notes.append(note)

# Bar 4: C7 (C, G, E, B), root (C) on beat 1, 3, 4

note = pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.5 + 0.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.0 + 0.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.5 + 0.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=6.0, end=6.0 + 0.25)
bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)

note = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.5 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.5 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.5 + 0.25)
piano.notes.append(note)

# Bar 3: Bb7 (Bb, D, F, A)

note = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.0 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.0 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.0 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.0 + 0.25)
piano.notes.append(note)

# Bar 4: C7 (C, E, G, B)

note = pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.5 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.5 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.5 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.5 + 0.25)
piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.05)
            drums.notes.append(note)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start motif

note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=1.75 + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.0 + 0.25)
sax.notes.append(note)

# Bar 3: Continue motif

note = pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.0 + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.25 + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=66, start=3.5, end=3.5 + 0.25)
sax.notes.append(note)

# Bar 4: Finish motif

note = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.5 + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=4.75 + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.0 + 0.25)
sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
