
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    time = i * 0.375
    if i % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.625),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.625, end=1.75),  # F2
    pretty_midi.Note(velocity=100, pitch=43, start=1.75, end=1.875),  # A2
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.75),
]
piano.notes.extend(piano_notes)

# Sax: Melody - short motif, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # E4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # G4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Dm7 -> Gm7 -> Cm7 -> F7
# Roots: D, G, C, F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.125),  # G2
    pretty_midi.Note(velocity=100, pitch=45, start=3.125, end=3.25),  # Bb2
    pretty_midi.Note(velocity=100, pitch=48, start=3.25, end=3.375),  # D3
    pretty_midi.Note(velocity=100, pitch=47, start=3.375, end=3.5),  # C3
]
bass.notes.extend(bass_notes)

# Piano: Gm7 (G, Bb, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # D5
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F7 (F, A, C, E)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.625),  # F3
    pretty_midi.Note(velocity=100, pitch=52, start=4.625, end=4.75),  # A3
    pretty_midi.Note(velocity=100, pitch=55, start=4.75, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.0),  # E4
]
bass.notes.extend(bass_notes)

# Piano: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75),
]
piano.notes.extend(piano_notes)

# Sax: Finish motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # F5
    pretty_midi.Note(velocity=100, pitch=72, start=4.75, end=5.0),  # G5
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
for i in range(8):
    time = 1.5 + i * 0.375
    if i % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
