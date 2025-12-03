
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
bar_duration = 1.5
for bar in range(1):
    start = bar * bar_duration
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    hihat1 = pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2 (1.5 - 3.0s)
start = 1.5
# D2 (MIDI 38) - root
bass_note1 = pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.375)
# F (MIDI 41) - third
bass_note2 = pretty_midi.Note(velocity=100, pitch=41, start=start + 0.375, end=start + 0.75)
# G2 (MIDI 43) - fifth
bass_note3 = pretty_midi.Note(velocity=100, pitch=43, start=start + 0.75, end=start + 1.125)
# E (MIDI 40) - chromatic approach
bass_note4 = pretty_midi.Note(velocity=100, pitch=40, start=start + 1.125, end=start + 1.5)
bass.notes.extend([bass_note1, bass_note2, bass_note3, bass_note4])

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2 (1.5 - 3.0s) - Dm7 (D-F-A-C)
piano_note1 = pretty_midi.Note(velocity=100, pitch=62, start=start, end=start + 0.75)
piano_note2 = pretty_midi.Note(velocity=100, pitch=65, start=start, end=start + 0.75)
piano_note3 = pretty_midi.Note(velocity=100, pitch=67, start=start, end=start + 0.75)
piano_note4 = pretty_midi.Note(velocity=100, pitch=69, start=start, end=start + 0.75)
piano.notes.extend([piano_note1, piano_note2, piano_note3, piano_note4])

# Bar 3 (3.0 - 4.5s) - G7 (G-B-D-F)
piano_note5 = pretty_midi.Note(velocity=100, pitch=67, start=start + 1.5, end=start + 2.25)
piano_note6 = pretty_midi.Note(velocity=100, pitch=71, start=start + 1.5, end=start + 2.25)
piano_note7 = pretty_midi.Note(velocity=100, pitch=69, start=start + 1.5, end=start + 2.25)
piano_note8 = pretty_midi.Note(velocity=100, pitch=65, start=start + 1.5, end=start + 2.25)
piano.notes.extend([piano_note5, piano_note6, piano_note7, piano_note8])

# Bar 4 (4.5 - 6.0s) - Cmaj7 (C-E-G-B)
piano_note9 = pretty_midi.Note(velocity=100, pitch=60, start=start + 3.0, end=start + 3.75)
piano_note10 = pretty_midi.Note(velocity=100, pitch=64, start=start + 3.0, end=start + 3.75)
piano_note11 = pretty_midi.Note(velocity=100, pitch=67, start=start + 3.0, end=start + 3.75)
piano_note12 = pretty_midi.Note(velocity=100, pitch=71, start=start + 3.0, end=start + 3.75)
piano.notes.extend([piano_note9, piano_note10, piano_note11, piano_note12])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2 (1.5 - 3.0s)
# Motif: D (MIDI 62) - F (MIDI 65) - E (MIDI 64) - D (MIDI 62)
sax_note1 = pretty_midi.Note(velocity=110, pitch=62, start=start, end=start + 0.375)
sax_note2 = pretty_midi.Note(velocity=110, pitch=65, start=start + 0.375, end=start + 0.75)
sax_note3 = pretty_midi.Note(velocity=110, pitch=64, start=start + 0.75, end=start + 1.125)
sax_note4 = pretty_midi.Note(velocity=110, pitch=62, start=start + 1.125, end=start + 1.5)
sax.notes.extend([sax_note1, sax_note2, sax_note3, sax_note4])

# Bar 3 (3.0 - 4.5s)
# Leave it hanging
# No notes

# Bar 4 (4.5 - 6.0s)
# Come back and finish it
# Motif: D (MIDI 62) - F (MIDI 65) - E (MIDI 64) - D (MIDI 62)
sax_note5 = pretty_midi.Note(velocity=110, pitch=62, start=start + 3.0, end=start + 3.375)
sax_note6 = pretty_midi.Note(velocity=110, pitch=65, start=start + 3.375, end=start + 3.75)
sax_note7 = pretty_midi.Note(velocity=110, pitch=64, start=start + 3.75, end=start + 4.125)
sax_note8 = pretty_midi.Note(velocity=110, pitch=62, start=start + 4.125, end=start + 4.5)
sax.notes.extend([sax_note5, sax_note6, sax_note7, sax_note8])

# Drums for bars 2-4 (1.5 - 6.0s)
for bar in range(2, 4):
    start = bar * bar_duration
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    hihat1 = pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
