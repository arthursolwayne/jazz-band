
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
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Fm7: F, C, Ab, D
        # Root: F (45), 5th: C (48), 9th: Ab (47), 13th: D (50)
        # Walk down from G (47) chromatic to F (45)
        bass_notes = [pretty_midi.Note(velocity=90, pitch=47, start=start, end=start + 0.375),
                      pretty_midi.Note(velocity=90, pitch=46, start=start + 0.375, end=start + 0.75),
                      pretty_midi.Note(velocity=90, pitch=45, start=start + 0.75, end=start + 1.125),
                      pretty_midi.Note(velocity=90, pitch=48, start=start + 1.125, end=start + 1.5)]
    elif bar == 3:
        # Bb7: Bb, F, Db, Ab
        # Root: Bb (46), 5th: F (48), 9th: Db (45), 13th: Ab (47)
        # Walk down from C (48) chromatic to Bb (46)
        bass_notes = [pretty_midi.Note(velocity=90, pitch=48, start=start, end=start + 0.375),
                      pretty_midi.Note(velocity=90, pitch=47, start=start + 0.375, end=start + 0.75),
                      pretty_midi.Note(velocity=90, pitch=46, start=start + 0.75, end=start + 1.125),
                      pretty_midi.Note(velocity=90, pitch=45, start=start + 1.125, end=start + 1.5)]
    elif bar == 4:
        # Eb7: Eb, Bb, G, D
        # Root: Eb (44), 5th: Bb (46), 9th: G (47), 13th: D (50)
        # Walk up from D (50) chromatic to Eb (44)
        bass_notes = [pretty_midi.Note(velocity=90, pitch=50, start=start, end=start + 0.375),
                      pretty_midi.Note(velocity=90, pitch=49, start=start + 0.375, end=start + 0.75),
                      pretty_midi.Note(velocity=90, pitch=48, start=start + 0.75, end=start + 1.125),
                      pretty_midi.Note(velocity=90, pitch=44, start=start + 1.125, end=start + 1.5)]
    for note in bass_notes:
        bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Fm7: F, Ab, C, D
        piano_notes = [pretty_midi.Note(velocity=100, pitch=45, start=start, end=start + 0.75),
                       pretty_midi.Note(velocity=100, pitch=47, start=start, end=start + 0.75),
                       pretty_midi.Note(velocity=100, pitch=48, start=start, end=start + 0.75),
                       pretty_midi.Note(velocity=100, pitch=50, start=start, end=start + 1.5)]
    elif bar == 3:
        # Bb7: Bb, D, F, Ab
        piano_notes = [pretty_midi.Note(velocity=100, pitch=46, start=start, end=start + 0.75),
                       pretty_midi.Note(velocity=100, pitch=50, start=start, end=start + 0.75),
                       pretty_midi.Note(velocity=100, pitch=48, start=start, end=start + 0.75),
                       pretty_midi.Note(velocity=100, pitch=47, start=start, end=start + 1.5)]
    elif bar == 4:
        # Eb7: Eb, G, Bb, D
        piano_notes = [pretty_midi.Note(velocity=100, pitch=44, start=start, end=start + 0.75),
                       pretty_midi.Note(velocity=100, pitch=47, start=start, end=start + 0.75),
                       pretty_midi.Note(velocity=100, pitch=46, start=start, end=start + 0.75),
                       pretty_midi.Note(velocity=100, pitch=50, start=start, end=start + 1.5)]
    for note in piano_notes:
        piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm: F, Ab, C, D
# Motif: F - Ab - C - D (45, 47, 48, 50)
# Start on F, leave it hanging at Ab
start = 1.5
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=45, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=110, pitch=47, start=start + 0.375, end=start + 0.75),
    pretty_midi.Note(velocity=110, pitch=48, start=start + 1.125, end=start + 1.5),
    pretty_midi.Note(velocity=110, pitch=50, start=start + 1.5, end=start + 1.875)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2
start = 1.5
for i in range(8):
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
    drums.notes.append(hihat)
kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
snare_2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
snare_4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
drums.notes.extend([kick_1, kick_3, snare_2, snare_4])

# Drums: Bar 3
start = 3.0
for i in range(8):
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
    drums.notes.append(hihat)
kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
snare_2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
snare_4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
drums.notes.extend([kick_1, kick_3, snare_2, snare_4])

# Drums: Bar 4
start = 4.5
for i in range(8):
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
    drums.notes.append(hihat)
kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
snare_2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
snare_4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
drums.notes.extend([kick_1, kick_3, snare_2, snare_4])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
