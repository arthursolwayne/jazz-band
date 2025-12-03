
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
    start = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: D2 - F#2 (chromatic up) - G2 - D2
# Bar 3: A2 - C2 (chromatic down) - B2 - A2
# Bar 4: D2 - F#2 (chromatic up) - G2 - D2
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        notes = [(38, start, start + 0.375), (40, start + 0.375, start + 0.75), (43, start + 0.75, start + 1.125), (38, start + 1.125, start + 1.5)]
    elif bar == 3:
        notes = [(45, start, start + 0.375), (42, start + 0.375, start + 0.75), (46, start + 0.75, start + 1.125), (45, start + 1.125, start + 1.5)]
    else:
        notes = [(38, start, start + 0.375), (40, start + 0.375, start + 0.75), (43, start + 0.75, start + 1.125), (38, start + 1.125, start + 1.5)]
    for pitch, note_start, note_end in notes:
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=note_start, end=note_end)
        bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, G)
# Bar 3: G7 (B, D, F#, G)
# Bar 4: Cm7 (Eb, G, C, Eb)
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        notes = [(58, start, start + 0.75), (62, start, start + 0.75), (67, start, start + 0.75), (71, start, start + 0.75)]
    elif bar == 3:
        notes = [(71, start, start + 0.75), (67, start, start + 0.75), (75, start, start + 0.75), (72, start, start + 0.75)]
    else:
        notes = [(64, start, start + 0.75), (72, start, start + 0.75), (60, start, start + 0.75), (64, start, start + 0.75)]
    for pitch, note_start, note_end in notes:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=note_start, end=note_end)
        piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Dante: Tenor sax - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62) - F (65) - G (67) - D (62) - F (65) - G (67) - D (62)
# Bar 2: D - F - G
# Bar 3: (rest) - (rest) - (rest)
# Bar 4: D - F - G - D

# Bar 2: D - F - G
start = 1.5
note1 = pretty_midi.Note(velocity=110, pitch=62, start=start, end=start + 0.375)
note2 = pretty_midi.Note(velocity=110, pitch=65, start=start + 0.375, end=start + 0.75)
note3 = pretty_midi.Note(velocity=110, pitch=67, start=start + 0.75, end=start + 1.125)
sax.notes.append(note1)
sax.notes.append(note2)
sax.notes.append(note3)

# Bar 3: rest
# Bar 4: D - F - G - D
start = 4.5
note4 = pretty_midi.Note(velocity=110, pitch=62, start=start, end=start + 0.375)
note5 = pretty_midi.Note(velocity=110, pitch=65, start=start + 0.375, end=start + 0.75)
note6 = pretty_midi.Note(velocity=110, pitch=67, start=start + 0.75, end=start + 1.125)
note7 = pretty_midi.Note(velocity=110, pitch=62, start=start + 1.125, end=start + 1.5)
sax.notes.append(note4)
sax.notes.append(note5)
sax.notes.append(note6)
sax.notes.append(note7)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
