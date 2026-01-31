
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
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
root = 50  # D2
fifth = 57  # A2
for bar in range(2, 5):
    start = bar * 1.5
    if bar % 2 == 0:
        # Root on 1, chromatic approach on 2, fifth on 3, chromatic approach on 4
        bass_note_1 = pretty_midi.Note(velocity=90, pitch=root, start=start, end=start + 0.375)
        bass_note_2 = pretty_midi.Note(velocity=90, pitch=root - 1, start=start + 0.375, end=start + 0.75)
        bass_note_3 = pretty_midi.Note(velocity=90, pitch=fifth, start=start + 0.75, end=start + 1.125)
        bass_note_4 = pretty_midi.Note(velocity=90, pitch=fifth + 1, start=start + 1.125, end=start + 1.5)
    else:
        # Fifth on 1, chromatic approach on 2, root on 3, chromatic approach on 4
        bass_note_1 = pretty_midi.Note(velocity=90, pitch=fifth, start=start, end=start + 0.375)
        bass_note_2 = pretty_midi.Note(velocity=90, pitch=fifth + 1, start=start + 0.375, end=start + 0.75)
        bass_note_3 = pretty_midi.Note(velocity=90, pitch=root, start=start + 0.75, end=start + 1.125)
        bass_note_4 = pretty_midi.Note(velocity=90, pitch=root - 1, start=start + 1.125, end=start + 1.5)
    bass.notes.extend([bass_note_1, bass_note_2, bass_note_3, bass_note_4])

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
# Bar 3: Bb7 (Bb-D-F-Ab)
# Bar 4: G7 (G-B-D-F)
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Dm7: D, F, A, C
        piano_note_1 = pretty_midi.Note(velocity=100, pitch=50, start=start, end=start + 0.75)
        piano_note_2 = pretty_midi.Note(velocity=100, pitch=53, start=start, end=start + 0.75)
        piano_note_3 = pretty_midi.Note(velocity=100, pitch=57, start=start, end=start + 0.75)
        piano_note_4 = pretty_midi.Note(velocity=100, pitch=60, start=start, end=start + 0.75)
    elif bar == 3:
        # Bb7: Bb, D, F, Ab
        piano_note_1 = pretty_midi.Note(velocity=100, pitch=46, start=start, end=start + 0.75)
        piano_note_2 = pretty_midi.Note(velocity=100, pitch=53, start=start, end=start + 0.75)
        piano_note_3 = pretty_midi.Note(velocity=100, pitch=57, start=start, end=start + 0.75)
        piano_note_4 = pretty_midi.Note(velocity=100, pitch=62, start=start, end=start + 0.75)
    elif bar == 4:
        # G7: G, B, D, F
        piano_note_1 = pretty_midi.Note(velocity=100, pitch=55, start=start, end=start + 0.75)
        piano_note_2 = pretty_midi.Note(velocity=100, pitch=59, start=start, end=start + 0.75)
        piano_note_3 = pretty_midi.Note(velocity=100, pitch=62, start=start, end=start + 0.75)
        piano_note_4 = pretty_midi.Note(velocity=100, pitch=67, start=start, end=start + 0.75)
    piano.notes.extend([piano_note_1, piano_note_2, piano_note_3, piano_note_4])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start motif (D, F, G)
# Bar 3: Leave it hanging (D)
# Bar 4: Resolve (C)
# Bar 2
sax_note_1 = pretty_midi.Note(velocity=110, pitch=50, start=1.5, end=1.5 + 0.375)
sax_note_2 = pretty_midi.Note(velocity=110, pitch=53, start=1.5 + 0.375, end=1.5 + 0.75)
sax_note_3 = pretty_midi.Note(velocity=110, pitch=55, start=1.5 + 0.75, end=1.5 + 1.125)
# Bar 3
sax_note_4 = pretty_midi.Note(velocity=110, pitch=50, start=3.0, end=3.0 + 0.375)
# Bar 4
sax_note_5 = pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.5 + 0.75)
sax.notes.extend([sax_note_1, sax_note_2, sax_note_3, sax_note_4, sax_note_5])

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
