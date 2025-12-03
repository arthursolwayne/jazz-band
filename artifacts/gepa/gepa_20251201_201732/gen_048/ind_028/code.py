
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
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

for i, time in enumerate([0.0, 0.75, 1.5]):
    if i < len(kick_notes):
        note = pretty_midi.Note(velocity=100, pitch=kick_notes[i], start=time, end=time + 0.375)
        drums.notes.append(note)

for i, time in enumerate([0.375, 1.125, 1.875]):
    if i < len(snare_notes):
        note = pretty_midi.Note(velocity=100, pitch=snare_notes[i], start=time, end=time + 0.375)
        drums.notes.append(note)

for i, time in enumerate([0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125]):
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1875)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: roots and fifths with chromatic approaches
# F7 -> Bb7 -> C7 -> E7
# Roots: F, Bb, C, E
# Fifths: C, F, G, B
# Chromatic approaches: E, A, Bb, D

# Bar 2 (1.5 - 3.0s)
# Root: F (48), fifth: C (60), chromatic approach: E (64)
note = pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=48, start=2.0, end=2.25)
bass.notes.append(note)

# Bar 3 (3.0 - 4.5s)
# Root: Bb (57), fifth: F (69), chromatic approach: A (65)
note = pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.5)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=57, start=3.5, end=3.75)
bass.notes.append(note)

# Bar 4 (4.5 - 6.0s)
# Root: C (60), fifth: G (67), chromatic approach: Bb (62)
note = pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=60, start=5.0, end=5.25)
bass.notes.append(note)

# Piano: Open voicings, resolve on the last bar
# Bar 2: F7 (F, A, C, E)
note = pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0)
piano.notes.append(note)

# Bar 3: Bb7 (Bb, D, F, A)
note = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=4.5)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5)
piano.notes.append(note)

# Bar 4: C7 (C, E, G, B)
note = pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0)
piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Start of motif
note = pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=2.0)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25)
sax.notes.append(note)

# Bar 3: Pause, leave it hanging
note = pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25)
sax.notes.append(note)

# Bar 4: Resolve the motif
note = pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=66, start=5.0, end=5.25)
sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

kick_notes = [36, 36, 36, 36]
snare_notes = [38, 38, 38, 38]

for i, time in enumerate([1.5, 2.25, 3.0, 3.75, 4.5, 5.25]):
    if i < len(kick_notes):
        note = pretty_midi.Note(velocity=100, pitch=kick_notes[i], start=time, end=time + 0.375)
        drums.notes.append(note)

for i, time in enumerate([1.875, 2.625, 3.375, 4.125, 4.875]):
    if i < len(snare_notes):
        note = pretty_midi.Note(velocity=100, pitch=snare_notes[i], start=time, end=time + 0.375)
        drums.notes.append(note)

for i, time in enumerate([1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125, 3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125, 4.5, 4.6875, 4.875, 5.0625]):
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1875)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.save('jazz_intro.mid')
