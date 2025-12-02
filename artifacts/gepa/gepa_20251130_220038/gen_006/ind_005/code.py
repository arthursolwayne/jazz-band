
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

bar1_start = 0.0
bar1_end = 1.5

# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 1.125, end=bar1_start + 1.5)

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=110, pitch=38, start=bar1_start + 0.75, end=bar1_start + 0.875)
snare2 = pretty_midi.Note(velocity=110, pitch=38, start=bar1_start + 1.875, end=bar1_start + 2.0)

# Hi-hat on every eighth
hihat_notes = []
for i in range(0, 4):
    start = bar1_start + (i * 0.375)
    end = start + 0.125
    hihat_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus - walking line, chromatic approaches
bass_notes = []

# F7 chord: F, A, C, E
# Walking line starting on G (chromatic approach)
bass_line = [71, 72, 71, 70, 69, 71, 72, 71]  # F7 chromatic approach walking line
for i, pitch in enumerate(bass_line):
    start = 1.5 + (i * 0.375)
    end = start + 0.375
    bass_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords on 2 and 4
piano_notes = []

# F7 chord: F, A, C, E
# Play on 2 and 4 of bars 2 and 3, and 2 of bar 4
chord_notes = [53, 56, 58, 60]  # F, A, C, E
for bar in range(2, 5):
    bar_start = 1.5 + ((bar - 2) * 1.5)
    for beat in [1, 3]:
        start = bar_start + (beat * 0.375)
        end = start + 0.375
        for pitch in chord_notes:
            piano_notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

piano.notes.extend(piano_notes)

# Sax: Dante - short motif, make it sing
# Motif: F (G) - Bb - C - F (G) (staccato or legato depending on feel)
# F = 65, Bb = 62, C = 67, G = 67 (chromatic approach)
# Start on bar 2, beat 1

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.5 + 0.125),  # G (chromatic approach)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5 + 0.375, end=1.5 + 0.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=1.5 + 0.75, end=1.5 + 0.875),  # C
    pretty_midi.Note(velocity=110, pitch=65, start=1.5 + 1.125, end=1.5 + 1.25)  # F
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
