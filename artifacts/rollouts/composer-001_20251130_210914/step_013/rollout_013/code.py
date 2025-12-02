
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
#ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on beat 0 and 2
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on beat 1 and 3
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Start with sax melody: 4 notes, short motif, D minor pentatonic with a twist

# Bar 2 (1.5 - 3.0s)
# Sax: D, F, G, Bb (Dm7)
note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25)
note3 = pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625)
note4 = pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0)
sax.notes.extend([note1, note2, note3, note4])

# Bass: Walking line, chromatic approach to D
# Bar 2: D, C#, D, Eb
note1 = pretty_midi.Note(velocity=70, pitch=62, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=70, pitch=61, start=1.875, end=2.25)
note3 = pretty_midi.Note(velocity=70, pitch=62, start=2.25, end=2.625)
note4 = pretty_midi.Note(velocity=70, pitch=60, start=2.625, end=3.0)
bass.notes.extend([note1, note2, note3, note4])

# Piano: D7 (F#, A, C#, D) on beat 2 and 4
note1 = pretty_midi.Note(velocity=80, pitch=66, start=1.875, end=2.25)
note2 = pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25)
note3 = pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25)
note4 = pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.25)
note5 = pretty_midi.Note(velocity=80, pitch=66, start=2.625, end=3.0)
note6 = pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0)
note7 = pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0)
note8 = pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0)
piano.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8])

# Bar 3 (3.0 - 4.5s)
# Sax: Repeat motif with a shift up a half-step
note1 = pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375)
note2 = pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75)
note3 = pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125)
note4 = pretty_midi.Note(velocity=100, pitch=68, start=4.125, end=4.5)
sax.notes.extend([note1, note2, note3, note4])

# Bass: Walking line, chromatic approach to E
# Bar 3: E, D#, E, F
note1 = pretty_midi.Note(velocity=70, pitch=64, start=3.0, end=3.375)
note2 = pretty_midi.Note(velocity=70, pitch=63, start=3.375, end=3.75)
note3 = pretty_midi.Note(velocity=70, pitch=64, start=3.75, end=4.125)
note4 = pretty_midi.Note(velocity=70, pitch=65, start=4.125, end=4.5)
bass.notes.extend([note1, note2, note3, note4])

# Piano: E7 (G#, B, D#, E) on beat 2 and 4
note1 = pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75)
note2 = pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75)
note3 = pretty_midi.Note(velocity=80, pitch=66, start=3.375, end=3.75)
note4 = pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75)
note5 = pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5)
note6 = pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5)
note7 = pretty_midi.Note(velocity=80, pitch=66, start=4.125, end=4.5)
note8 = pretty_midi.Note(velocity=80, pitch=64, start=4.125, end=4.5)
piano.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8])

# Bar 4 (4.5 - 6.0s)
# Sax: Repeat motif in D, ending on C
note1 = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875)
note2 = pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25)
note3 = pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625)
note4 = pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0)
sax.notes.extend([note1, note2, note3, note4])

# Bass: Walking line, chromatic approach to D
# Bar 4: D, C#, D, Eb
note1 = pretty_midi.Note(velocity=70, pitch=62, start=4.5, end=4.875)
note2 = pretty_midi.Note(velocity=70, pitch=61, start=4.875, end=5.25)
note3 = pretty_midi.Note(velocity=70, pitch=62, start=5.25, end=5.625)
note4 = pretty_midi.Note(velocity=70, pitch=60, start=5.625, end=6.0)
bass.notes.extend([note1, note2, note3, note4])

# Piano: D7 (F#, A, C#, D) on beat 2 and 4
note1 = pretty_midi.Note(velocity=80, pitch=66, start=4.875, end=5.25)
note2 = pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25)
note3 = pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25)
note4 = pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25)
note5 = pretty_midi.Note(velocity=80, pitch=66, start=5.625, end=6.0)
note6 = pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0)
note7 = pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0)
note8 = pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0)
piano.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8])

# Drums: continue in bar 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on beat 0 and 2
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on beat 1 and 3
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
