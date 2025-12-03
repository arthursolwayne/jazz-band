
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on beat 1 and 3
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on beat 2 and 4
    snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bar 2: Diane on piano
bar = 1
start = bar * 1.5
# Fm7 - Bb7 - Eb7 - Ab7
# Open voicings, resolve on the last chord
# Fm7: F, Ab, C, Db
note1 = pretty_midi.Note(velocity=100, pitch=71, start=start, end=start + 0.75)
note2 = pretty_midi.Note(velocity=100, pitch=67, start=start, end=start + 0.75)
note3 = pretty_midi.Note(velocity=100, pitch=64, start=start, end=start + 0.75)
note4 = pretty_midi.Note(velocity=100, pitch=62, start=start, end=start + 0.75)
piano.notes.extend([note1, note2, note3, note4])

# Marcus on bass: walking line, roots and fifths with chromatic approaches
# Fm: F, C, Bb, Eb
note1 = pretty_midi.Note(velocity=90, pitch=70, start=start, end=start + 0.375)
note2 = pretty_midi.Note(velocity=90, pitch=76, start=start + 0.375, end=start + 0.75)
note3 = pretty_midi.Note(velocity=90, pitch=74, start=start + 0.75, end=start + 1.125)
note4 = pretty_midi.Note(velocity=90, pitch=67, start=start + 1.125, end=start + 1.5)
bass.notes.extend([note1, note2, note3, note4])

# Bar 3: Diane on piano
bar = 2
start = bar * 1.5
# Bb7: Bb, D, F, Ab
note1 = pretty_midi.Note(velocity=100, pitch=69, start=start, end=start + 0.75)
note2 = pretty_midi.Note(velocity=100, pitch=64, start=start, end=start + 0.75)
note3 = pretty_midi.Note(velocity=100, pitch=71, start=start, end=start + 0.75)
note4 = pretty_midi.Note(velocity=100, pitch=67, start=start, end=start + 0.75)
piano.notes.extend([note1, note2, note3, note4])

# Marcus on bass: walking line, roots and fifths with chromatic approaches
# Bb7: Bb, F, Eb, Ab
note1 = pretty_midi.Note(velocity=90, pitch=69, start=start, end=start + 0.375)
note2 = pretty_midi.Note(velocity=90, pitch=71, start=start + 0.375, end=start + 0.75)
note3 = pretty_midi.Note(velocity=90, pitch=67, start=start + 0.75, end=start + 1.125)
note4 = pretty_midi.Note(velocity=90, pitch=66, start=start + 1.125, end=start + 1.5)
bass.notes.extend([note1, note2, note3, note4])

# Bar 4: Diane on piano
bar = 3
start = bar * 1.5
# Eb7: Eb, G, Bb, Db
note1 = pretty_midi.Note(velocity=100, pitch=65, start=start, end=start + 0.75)
note2 = pretty_midi.Note(velocity=100, pitch=69, start=start, end=start + 0.75)
note3 = pretty_midi.Note(velocity=100, pitch=69, start=start, end=start + 0.75)
note4 = pretty_midi.Note(velocity=100, pitch=62, start=start, end=start + 0.75)
piano.notes.extend([note1, note2, note3, note4])

# Marcus on bass: walking line, roots and fifths with chromatic approaches
# Eb7: Eb, Bb, Ab, Db
note1 = pretty_midi.Note(velocity=90, pitch=65, start=start, end=start + 0.375)
note2 = pretty_midi.Note(velocity=90, pitch=69, start=start + 0.375, end=start + 0.75)
note3 = pretty_midi.Note(velocity=90, pitch=67, start=start + 0.75, end=start + 1.125)
note4 = pretty_midi.Note(velocity=90, pitch=62, start=start + 1.125, end=start + 1.5)
bass.notes.extend([note1, note2, note3, note4])

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Eb, F
bar = 1
start = bar * 1.5
note1 = pretty_midi.Note(velocity=110, pitch=71, start=start, end=start + 0.375)
note2 = pretty_midi.Note(velocity=110, pitch=67, start=start + 0.375, end=start + 0.75)
note3 = pretty_midi.Note(velocity=110, pitch=65, start=start + 0.75, end=start + 1.125)
note4 = pretty_midi.Note(velocity=110, pitch=71, start=start + 1.5, end=start + 1.875)
sax.notes.extend([note1, note2, note3, note4])

# Drums for bars 2-4
for bar in range(1, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4])

# Save the MIDI file
midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
