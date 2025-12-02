
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
for beat in range(4):
    time = beat * 0.375
    # Kick on 1 and 3
    if beat % 2 == 0:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    # Snare on 2 and 4
    if beat % 2 == 1:
        drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125))
    # Hi-hat on every eighth
    drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125))
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = []
bass_chords = [
    # Bar 2: F7 (F, A, C, E♭)
    [71, 69, 67, 64],
    # Bar 3: B♭7 (B♭, D, F, A♭)
    [67, 62, 67, 60],
    # Bar 4: E♭7 (E♭, G, B♭, D♭)
    [64, 69, 67, 60],
]
for bar in range(2, 5):
    start_time = (bar - 1) * 1.5
    for beat in range(4):
        time = start_time + beat * 0.375
        root = bass_chords[bar - 2][0]
        # Chromatic approach to root
        if beat == 0:
            bass_notes.append(pretty_midi.Note(velocity=100, pitch=root - 1, start=time, end=time + 0.125))
        elif beat == 1:
            bass_notes.append(pretty_midi.Note(velocity=100, pitch=root + 2, start=time, end=time + 0.125))
        elif beat == 2:
            bass_notes.append(pretty_midi.Note(velocity=100, pitch=root, start=time, end=time + 0.125))
        elif beat == 3:
            bass_notes.append(pretty_midi.Note(velocity=100, pitch=root + 1, start=time, end=time + 0.125))
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = []
for bar in range(2, 5):
    start_time = (bar - 1) * 1.5
    chord = bass_chords[bar - 2]
    # Comp on 2 and 4
    for beat in range(4):
        time = start_time + beat * 0.375
        if beat in [1, 3]:
            # 7th chord
            for note in chord:
                piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))
            # Add 7th
            if bar == 2:
                piano_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=time, end=time + 0.125))
            elif bar == 3:
                piano_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=time, end=time + 0.125))
            elif bar == 4:
                piano_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=time, end=time + 0.125))
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = []
# Bar 2
start_time = 1.5
# F (66) to E♭ (64) to D (62) to C (60)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=66, start=start_time, end=start_time + 0.25))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=64, start=start_time + 0.25, end=start_time + 0.5))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=start_time + 0.5, end=start_time + 0.75))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=60, start=start_time + 0.75, end=start_time + 1.0))

# Bar 3: Leave it hanging, rest
sax_notes.append(pretty_midi.Note(velocity=60, pitch=60, start=start_time + 1.0, end=start_time + 1.5))

# Bar 4: Come back and finish it
sax_notes.append(pretty_midi.Note(velocity=110, pitch=66, start=start_time + 2.5, end=start_time + 2.75))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=64, start=start_time + 2.75, end=start_time + 3.0))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=start_time + 3.0, end=start_time + 3.25))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=60, start=start_time + 3.25, end=start_time + 3.5))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=start_time + 3.5, end=start_time + 3.75))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=64, start=start_time + 3.75, end=start_time + 4.0))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=66, start=start_time + 4.0, end=start_time + 4.25))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=67, start=start_time + 4.25, end=start_time + 4.5))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=69, start=start_time + 4.5, end=start_time + 4.75))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=67, start=start_time + 4.75, end=start_time + 5.0))

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
