
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
    start_time = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.75, end=start_time + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.375, end=start_time + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.125, end=start_time + 1.5)
    # Hi-hat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start_time + i * 0.375, end=start_time + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Sax: Short motif starting on Fm (F, Ab, Bb, D), then leave it hanging
# Start on bar 2, beat 1: F (65), Ab (67), Bb (62), D (67)
# Then repeat the first two notes on bar 3, beat 1, and resolve on bar 4, beat 3 with a Bb (62)

# Bar 2, beat 1
sax_note1 = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875)
sax_note2 = pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25)
sax_note3 = pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625)
sax_note4 = pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0)
sax.notes.extend([sax_note1, sax_note2, sax_note3, sax_note4])

# Bar 3, beat 1
sax_note5 = pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375)
sax_note6 = pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75)
sax.notes.extend([sax_note5, sax_note6])

# Bar 4, beat 3
sax_note7 = pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5)
sax.notes.append(sax_note7)

# Bass: Walking line, chromatic approaches, never the same note twice
# Fm7: F, Ab, Bb, D
# Walking line: F, Gb (chromatic), G, Ab
# Bar 2: F, Gb, G, Ab (beat 1-4)
# Bar 3: Bb, B, C, C# (beat 1-4)
# Bar 4: D, Eb, E, F (beat 1-4)

# Bar 2
bass_note1 = pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875)
bass_note2 = pretty_midi.Note(velocity=80, pitch=66, start=1.875, end=2.25)
bass_note3 = pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625)
bass_note4 = pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0)
bass.notes.extend([bass_note1, bass_note2, bass_note3, bass_note4])

# Bar 3
bass_note5 = pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375)
bass_note6 = pretty_midi.Note(velocity=80, pitch=63, start=3.375, end=3.75)
bass_note7 = pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125)
bass_note8 = pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5)
bass.notes.extend([bass_note5, bass_note6, bass_note7, bass_note8])

# Bar 4
bass_note9 = pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875)
bass_note10 = pretty_midi.Note(velocity=80, pitch=68, start=4.875, end=5.25)
bass_note11 = pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625)
bass_note12 = pretty_midi.Note(velocity=80, pitch=70, start=5.625, end=6.0)
bass.notes.extend([bass_note9, bass_note10, bass_note11, bass_note12])

# Piano: 7th chords, comp on 2 and 4
# Bar 2: Fm7 (F, Ab, Bb, D) on beat 2
# Bar 3: D7 (D, F#, A, C) on beat 2
# Bar 4: Fm7 (F, Ab, Bb, D) on beat 2

# Bar 2, beat 2
piano_note1 = pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625)
piano_note2 = pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625)
piano_note3 = pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625)
piano_note4 = pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625)
piano.notes.extend([piano_note1, piano_note2, piano_note3, piano_note4])

# Bar 3, beat 2
piano_note5 = pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125)
piano_note6 = pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125)
piano_note7 = pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125)
piano_note8 = pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=4.125)
piano.notes.extend([piano_note5, piano_note6, piano_note7, piano_note8])

# Bar 4, beat 2
piano_note9 = pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25)
piano_note10 = pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25)
piano_note11 = pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25)
piano_note12 = pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25)
piano.notes.extend([piano_note9, piano_note10, piano_note11, piano_note12])

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start_time = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.75, end=start_time + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.375, end=start_time + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.125, end=start_time + 1.5)
    # Hi-hat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start_time + i * 0.375, end=start_time + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
