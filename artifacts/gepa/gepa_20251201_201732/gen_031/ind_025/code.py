
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
drum_notes = []
# Kick on 1 and 3
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))
# Snare on 2 and 4
drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))
# Hi-hat on every eighth
for i in range(0, 4):
    drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=i*0.375, end=(i+1)*0.375))
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = []
# Bar 2: F - G - A - Bb
bass_notes.append(pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.875))  # F
bass_notes.append(pretty_midi.Note(velocity=80, pitch=74, start=1.875, end=2.25)) # G
bass_notes.append(pretty_midi.Note(velocity=80, pitch=76, start=2.25, end=2.625)) # A
bass_notes.append(pretty_midi.Note(velocity=80, pitch=77, start=2.625, end=3.0))  # Bb

# Bar 3: Bb - C - D - Eb
bass_notes.append(pretty_midi.Note(velocity=80, pitch=77, start=3.0, end=3.375))  # Bb
bass_notes.append(pretty_midi.Note(velocity=80, pitch=79, start=3.375, end=3.75)) # C
bass_notes.append(pretty_midi.Note(velocity=80, pitch=81, start=3.75, end=4.125)) # D
bass_notes.append(pretty_midi.Note(velocity=80, pitch=83, start=4.125, end=4.5))  # Eb

# Bar 4: Eb - F - G - A
bass_notes.append(pretty_midi.Note(velocity=80, pitch=83, start=4.5, end=4.875))  # Eb
bass_notes.append(pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.25)) # F
bass_notes.append(pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.625)) # G
bass_notes.append(pretty_midi.Note(velocity=80, pitch=76, start=5.625, end=6.0))  # A
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.875)  # F
]
# Bar 3: Bb7
piano_notes.append(pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375))  # Bb
piano_notes.append(pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.375))  # D
piano_notes.append(pretty_midi.Note(velocity=100, pitch=86, start=3.0, end=3.375))  # F
piano_notes.append(pretty_midi.Note(velocity=100, pitch=89, start=3.0, end=3.375))  # A
# Bar 4: Eb7
piano_notes.append(pretty_midi.Note(velocity=100, pitch=83, start=4.5, end=4.875))  # Eb
piano_notes.append(pretty_midi.Note(velocity=100, pitch=88, start=4.5, end=4.875))  # G
piano_notes.append(pretty_midi.Note(velocity=100, pitch=92, start=4.5, end=4.875))  # Bb
piano_notes.append(pretty_midi.Note(velocity=100, pitch=95, start=4.5, end=4.875))  # D
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - G - F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=100, pitch=77, start=1.625, end=1.75), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=1.75, end=1.875), # G
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0)   # F
]
# Second phrase: F - Eb - D - F
sax_notes.append(pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.375)) # F
sax_notes.append(pretty_midi.Note(velocity=100, pitch=83, start=2.375, end=2.5))  # Eb
sax_notes.append(pretty_midi.Note(velocity=100, pitch=81, start=2.5, end=2.625))  # D
sax_notes.append(pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=2.75)) # F
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 4):
    start = bar * 1.5
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
# Snare on 2 and 4
for bar in range(2, 4):
    start = bar * 1.5
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0))
# Hi-hat on every eighth
for bar in range(2, 4):
    for i in range(0, 4):
        drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=bar * 1.5 + i * 0.375, end=bar * 1.5 + (i + 1) * 0.375))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
