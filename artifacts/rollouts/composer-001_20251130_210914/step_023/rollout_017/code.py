
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
    kick1 = pretty_midi.Note(velocity=110, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=110, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i*0.375, end=start + i*0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# BASS LINE: Walking line with chromatic approaches
# D Dorian: D, E, F#, G, A, B, C
# Bass line in D (1st bar of section)
for bar in range(3):
    start = 1.5 + bar * 1.5
    # Bass note on beat 1
    note1 = pretty_midi.Note(velocity=90, pitch=62, start=start, end=start + 0.375)
    # Chromatic approach on beat 2
    note2 = pretty_midi.Note(velocity=90, pitch=61, start=start + 0.375, end=start + 0.75)
    # Bass note on beat 3
    note3 = pretty_midi.Note(velocity=90, pitch=64, start=start + 0.75, end=start + 1.125)
    # Chromatic approach on beat 4
    note4 = pretty_midi.Note(velocity=90, pitch=65, start=start + 1.125, end=start + 1.5)
    bass.notes.extend([note1, note2, note3, note4])

# PIANO: 7th chords, comp on 2 and 4
for bar in range(3):
    start = 1.5 + bar * 1.5
    # D7 on beat 1 (D, F#, A, C)
    chord1 = [pretty_midi.Note(velocity=80, pitch=62, start=start, end=start + 0.375),
              pretty_midi.Note(velocity=80, pitch=67, start=start, end=start + 0.375),
              pretty_midi.Note(velocity=80, pitch=69, start=start, end=start + 0.375),
              pretty_midi.Note(velocity=80, pitch=64, start=start, end=start + 0.375)]
    # D7 on beat 3
    chord3 = [pretty_midi.Note(velocity=80, pitch=62, start=start + 0.75, end=start + 1.125),
              pretty_midi.Note(velocity=80, pitch=67, start=start + 0.75, end=start + 1.125),
              pretty_midi.Note(velocity=80, pitch=69, start=start + 0.75, end=start + 1.125),
              pretty_midi.Note(velocity=80, pitch=64, start=start + 0.75, end=start + 1.125)]
    piano.notes.extend(chord1 + chord3)

# SAX: Motif in D, one phrase, leave it hanging
# Dorian scale: D, E, F#, G, A, B, C
# Phrase: D - F# - G - D (start on beat 1 of bar 2)
note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375)
note2 = pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 0.375, end=1.5 + 0.75)
note3 = pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 0.75, end=1.5 + 1.125)
note4 = pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 1.125, end=1.5 + 1.5)
sax.notes.extend([note1, note2, note3, note4])

# Repeat motif in bar 3
note1 = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.0 + 0.375)
note2 = pretty_midi.Note(velocity=100, pitch=67, start=3.0 + 0.375, end=3.0 + 0.75)
note3 = pretty_midi.Note(velocity=100, pitch=69, start=3.0 + 0.75, end=3.0 + 1.125)
note4 = pretty_midi.Note(velocity=100, pitch=62, start=3.0 + 1.125, end=3.0 + 1.5)
sax.notes.extend([note1, note2, note3, note4])

# Repeat motif in bar 4
note1 = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.5 + 0.375)
note2 = pretty_midi.Note(velocity=100, pitch=67, start=4.5 + 0.375, end=4.5 + 0.75)
note3 = pretty_midi.Note(velocity=100, pitch=69, start=4.5 + 0.75, end=4.5 + 1.125)
note4 = pretty_midi.Note(velocity=100, pitch=62, start=4.5 + 1.125, end=4.5 + 1.5)
sax.notes.extend([note1, note2, note3, note4])

# Drums in bars 2-4: same pattern as bar 1
for bar in range(3):
    start = 1.5 + bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=110, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=110, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i*0.375, end=start + i*0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
