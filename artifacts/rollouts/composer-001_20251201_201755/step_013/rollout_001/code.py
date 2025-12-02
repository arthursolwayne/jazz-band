
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
    # Kick on beat 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.append(kick)
    drums.notes.append(snare)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, D2-G2, roots and fifths with chromatic approaches
for bar in range(2, 5):
    start = bar * 1.5
    # D2 (D2 = MIDI 38)
    note1 = pretty_midi.Note(velocity=90, pitch=38, start=start, end=start + 0.375)
    # F#2 (D2 + minor third, chromatic approach)
    note2 = pretty_midi.Note(velocity=90, pitch=40, start=start + 0.375, end=start + 0.75)
    # G2 (fifth of D)
    note3 = pretty_midi.Note(velocity=90, pitch=43, start=start + 0.75, end=start + 1.125)
    # D2 again
    note4 = pretty_midi.Note(velocity=90, pitch=38, start=start + 1.125, end=start + 1.5)
    bass.notes.append(note1)
    bass.notes.append(note2)
    bass.notes.append(note3)
    bass.notes.append(note4)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
note1 = pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.875)
note3 = pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875)
note4 = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875)
piano.notes.append(note1)
piano.notes.append(note2)
piano.notes.append(note3)
piano.notes.append(note4)

# Bar 3: Gm7 (G Bb D F)
note1 = pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375)
note2 = pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375)
note3 = pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375)
note4 = pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375)
piano.notes.append(note1)
piano.notes.append(note2)
piano.notes.append(note3)
piano.notes.append(note4)

# Bar 4: C7 (C E G Bb)
note1 = pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875)
note2 = pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875)
note3 = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875)
note4 = pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875)
piano.notes.append(note1)
piano.notes.append(note2)
piano.notes.append(note3)
piano.notes.append(note4)

# Dante: Tenor sax melody (One short motif, make it sing)
# Bar 2: E (MIDI 64) on beat 1
note1 = pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875)
# Bar 2: D (MIDI 62) on beat 2
note2 = pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25)
# Bar 3: F (MIDI 65) on beat 1
note3 = pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375)
# Bar 3: E (MIDI 64) on beat 2
note4 = pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75)
# Bar 4: G (MIDI 67) on beat 1
note5 = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875)
# Bar 4: F (MIDI 65) on beat 2 (resolve)
note6 = pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25)
sax.notes.append(note1)
sax.notes.append(note2)
sax.notes.append(note3)
sax.notes.append(note4)
sax.notes.append(note5)
sax.notes.append(note6)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
