
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

# Kick on 1 and 3
drum_kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.extend([drum_kick_1, drum_kick_3])

# Snare on 2 and 4
drum_snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drums.notes.extend([drum_snare_2, drum_snare_4])

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.375
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: Dm7 (D, F, A, C)
bass_note_2 = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)
bass_note_3 = pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25)
bass_note_4 = pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625)
bass_note_5 = pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0)
bass.notes.extend([bass_note_2, bass_note_3, bass_note_4, bass_note_5])

# Bar 3: G7 (G, B, D, F)
bass_note_6 = pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375)
bass_note_7 = pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.75)
bass_note_8 = pretty_midi.Note(velocity=100, pitch=47, start=3.75, end=4.125)
bass_note_9 = pretty_midi.Note(velocity=100, pitch=48, start=4.125, end=4.5)
bass.notes.extend([bass_note_6, bass_note_7, bass_note_8, bass_note_9])

# Bar 4: Cm7 (C, Eb, G, Bb)
bass_note_10 = pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.875)
bass_note_11 = pretty_midi.Note(velocity=100, pitch=45, start=4.875, end=5.25)
bass_note_12 = pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625)
bass_note_13 = pretty_midi.Note(velocity=100, pitch=45, start=5.625, end=6.0)
bass.notes.extend([bass_note_10, bass_note_11, bass_note_12, bass_note_13])

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_note_2 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)
piano_note_3 = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875)
piano_note_4 = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875)
piano_note_5 = pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875)
piano.notes.extend([piano_note_2, piano_note_3, piano_note_4, piano_note_5])

# Bar 3: G7 (G, B, D, F)
piano_note_6 = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375)
piano_note_7 = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375)
piano_note_8 = pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375)
piano_note_9 = pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375)
piano.notes.extend([piano_note_6, piano_note_7, piano_note_8, piano_note_9])

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_note_10 = pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875)
piano_note_11 = pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875)
piano_note_12 = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875)
piano_note_13 = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875)
piano.notes.extend([piano_note_10, piano_note_11, piano_note_12, piano_note_13])

# You: Tenor Sax - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F (65), D (62), leave hanging on F (65) at end of bar 2
# Then come back with G (67), A (69), Bb (71), C (72) to resolve

# Bar 2: D (62), F (65), D (62)
sax_note_1 = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75)
sax_note_2 = pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0)
sax_note_3 = pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25)
sax.notes.extend([sax_note_1, sax_note_2, sax_note_3])

# Bar 3: G (67), A (69), Bb (71)
sax_note_4 = pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25)
sax_note_5 = pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5)
sax_note_6 = pretty_midi.Note(velocity=110, pitch=71, start=3.5, end=3.75)
sax.notes.extend([sax_note_4, sax_note_5, sax_note_6])

# Bar 4: C (72), resolve on C (72)
sax_note_7 = pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.75)
sax_note_8 = pretty_midi.Note(velocity=110, pitch=72, start=4.75, end=5.0)
sax.notes.extend([sax_note_7, sax_note_8])

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    kick_start = bar * 1.5
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=kick_start + 1.125, end=kick_start + 1.5)
    drums.notes.extend([kick_1, kick_3])

# Snare on 2 and 4
for bar in range(2, 5):
    snare_start = bar * 1.5
    snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=snare_start + 0.75, end=snare_start + 1.125)
    snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=snare_start + 1.875, end=snare_start + 2.25)
    drums.notes.extend([snare_2, snare_4])

# Hi-hat on every eighth
for bar in range(2, 5):
    for i in range(0, 4):
        start = bar * 1.5 + i * 0.375
        end = start + 0.375
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
