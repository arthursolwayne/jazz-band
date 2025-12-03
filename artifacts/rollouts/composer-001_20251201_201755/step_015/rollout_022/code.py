
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
bar_duration = 1.5
time = 0.0

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = beat * bar_duration / 4
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
time = 1.5

# Bass: Walking line in F (F2, A2, C3, D3), chromatic approach to C3
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=time, end=time + 0.375),  # F2
    pretty_midi.Note(velocity=100, pitch=55, start=time + 0.375, end=time + 0.75),  # A2
    pretty_midi.Note(velocity=100, pitch=57, start=time + 0.75, end=time + 1.125),  # C3
    pretty_midi.Note(velocity=100, pitch=58, start=time + 1.125, end=time + 1.5),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=time, end=time + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=time, end=time + 0.375),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=time, end=time + 0.375),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=time, end=time + 0.375),  # E
]
piano.notes.extend(piano_notes)

# Sax: Start of motif
# F - Bb - C - D (sax in Bb, so F is D)
note = pretty_midi.Note(velocity=110, pitch=62, start=time, end=time + 0.375)  # D (F on sax)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=67, start=time + 0.375, end=time + 0.75)  # G (Bb on sax)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=69, start=time + 0.75, end=time + 1.125)  # A (C on sax)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=71, start=time + 1.125, end=time + 1.5)  # B (D on sax)
sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
time = 3.0

# Bass: Walking line in F (F2, A2, C3, D3), chromatic approach to C3
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=time, end=time + 0.375),  # F2
    pretty_midi.Note(velocity=100, pitch=55, start=time + 0.375, end=time + 0.75),  # A2
    pretty_midi.Note(velocity=100, pitch=57, start=time + 0.75, end=time + 1.125),  # C3
    pretty_midi.Note(velocity=100, pitch=58, start=time + 1.125, end=time + 1.5),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bbmaj7 (Bb, D, F, A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=time, end=time + 0.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=time, end=time + 0.375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=time, end=time + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=time, end=time + 0.375),  # A
]
piano.notes.extend(piano_notes)

# Sax: Continue motif
# Bb - C - D - F (sax in Bb, so Bb is G, C is A, D is B, F is D)
note = pretty_midi.Note(velocity=110, pitch=67, start=time, end=time + 0.375)  # G (Bb on sax)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=69, start=time + 0.375, end=time + 0.75)  # A (C on sax)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=71, start=time + 0.75, end=time + 1.125)  # B (D on sax)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=62, start=time + 1.125, end=time + 1.5)  # D (F on sax)
sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
time = 4.5

# Bass: Walking line in F (F2, A2, C3, D3), chromatic approach to C3
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=time, end=time + 0.375),  # F2
    pretty_midi.Note(velocity=100, pitch=55, start=time + 0.375, end=time + 0.75),  # A2
    pretty_midi.Note(velocity=100, pitch=57, start=time + 0.75, end=time + 1.125),  # C3
    pretty_midi.Note(velocity=100, pitch=58, start=time + 1.125, end=time + 1.5),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=time, end=time + 0.375),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=time, end=time + 0.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=time, end=time + 0.375),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=time, end=time + 0.375),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Finish motif
# C - D - F - (rest)
note = pretty_midi.Note(velocity=110, pitch=69, start=time, end=time + 0.375)  # A (C on sax)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=71, start=time + 0.375, end=time + 0.75)  # B (D on sax)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=62, start=time + 0.75, end=time + 1.125)  # D (F on sax)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=62, start=time + 1.125, end=time + 1.5)  # D (F on sax)
sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = beat * bar_duration / 4 + 1.5
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
