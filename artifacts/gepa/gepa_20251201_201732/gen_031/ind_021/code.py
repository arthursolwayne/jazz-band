
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
drum_note_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)  # Kick on 1
drum_note_2 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)  # Snare on 2
drum_note_3 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)  # Kick on 3
drum_note_4 = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)  # Hihat on every eighth
drums.notes.extend([drum_note_1, drum_note_2, drum_note_3, drum_note_4])

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Dm7 -> Gm7 -> Am7 -> Dm7 (motif)
sax_note_1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75)  # D (Dm7)
sax_note_2 = pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25)  # G (Gm7)
sax_note_3 = pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75)  # A (Am7)
sax_note_4 = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25)  # D (Dm7)
sax.notes.extend([sax_note_1, sax_note_2, sax_note_3, sax_note_4])

# Bass: Walking line in Dm
bass_note_1 = pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75)  # D
bass_note_2 = pretty_midi.Note(velocity=80, pitch=53, start=1.75, end=2.0)  # F
bass_note_3 = pretty_midi.Note(velocity=80, pitch=52, start=2.0, end=2.25)  # E
bass_note_4 = pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.5)  # D
bass_note_5 = pretty_midi.Note(velocity=80, pitch=55, start=2.5, end=2.75)  # G
bass_note_6 = pretty_midi.Note(velocity=80, pitch=57, start=2.75, end=3.0)  # A
bass_note_7 = pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.25)  # G
bass_note_8 = pretty_midi.Note(velocity=80, pitch=50, start=3.25, end=3.5)  # D
bass.notes.extend([bass_note_1, bass_note_2, bass_note_3, bass_note_4, bass_note_5, bass_note_6, bass_note_7, bass_note_8])

# Piano: Open voicings, different chord each bar
# Bar 2: Dm7 (D, F, A, C)
piano_note_1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0)
piano_note_2 = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0)
piano_note_3 = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0)
piano_note_4 = pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0)
piano.notes.extend([piano_note_1, piano_note_2, piano_note_3, piano_note_4])

# Bar 3: Gm7 (G, Bb, D, F)
piano_note_5 = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5)
piano_note_6 = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5)
piano_note_7 = pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5)
piano_note_8 = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5)
piano.notes.extend([piano_note_5, piano_note_6, piano_note_7, piano_note_8])

# Bar 4: Am7 (A, C, E, G)
piano_note_9 = pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0)
piano_note_10 = pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0)
piano_note_11 = pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0)
piano_note_12 = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0)
piano.notes.extend([piano_note_9, piano_note_10, piano_note_11, piano_note_12])

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    start = (bar - 1) * 1.5
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5)
    drums.notes.extend([kick_1, snare_2, kick_3, hihat])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
