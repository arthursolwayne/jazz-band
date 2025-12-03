
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

# Kick on 1 and 3, Snare on 2 and 4, Hihat on every eighth
for beat in [0, 2]:  # 1 and 3
    note = pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
for beat in [1, 3]:  # 2 and 4
    note = pretty_midi.Note(velocity=110, pitch=38, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
for beat in range(4):  # every eighth
    note = pretty_midi.Note(velocity=80, pitch=42, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: F7 - D2, F2, E2 (chromatic approach), G2
note = pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=39, start=2.25, end=2.625)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
bass.notes.append(note)

# Bar 3: Bb7 - G2, Bb2, A2, B2
note = pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=45, start=4.125, end=4.5)
bass.notes.append(note)

# Bar 4: E7 - D2, E2, D2, F2
note = pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.625)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, Eb) - open voicing
note = pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=3.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=68, start=1.5, end=3.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=3.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0)
piano.notes.append(note)

# Bar 3: Bb7 (Bb, D, F, Ab) - open voicing
note = pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=4.5)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=4.5)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=4.5)
piano.notes.append(note)

# Bar 4: E7 (E, G#, B, D) - open voicing
note = pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=6.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=6.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=6.0)
piano.notes.append(note)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: F (65), A (68), F (65), G (67)
note = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0)
sax.notes.append(note)

# Bar 3: Bb (61), D (64), Bb (61), C (65)
note = pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5)
sax.notes.append(note)

# Bar 4: E (69), G# (71), E (69), F (66)
note = pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0)
sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, Snare on 2 and 4, Hihat on every eighth
for bar in range(2, 4):
    for beat in [0, 2]:  # 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=36, start=(bar * 1.5) + (beat * 0.375), end=(bar * 1.5) + (beat + 1) * 0.375)
        drums.notes.append(note)
    for beat in [1, 3]:  # 2 and 4
        note = pretty_midi.Note(velocity=110, pitch=38, start=(bar * 1.5) + (beat * 0.375), end=(bar * 1.5) + (beat + 1) * 0.375)
        drums.notes.append(note)
    for beat in range(4):  # every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=(bar * 1.5) + (beat * 0.375), end=(bar * 1.5) + (beat + 1) * 0.375)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
