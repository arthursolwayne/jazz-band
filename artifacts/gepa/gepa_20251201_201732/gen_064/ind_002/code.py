
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
drum_notes = []
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 2 and 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))
    # Hi-hat on every eighth
    for i in range(8):
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line in Fm, roots and fifths with chromatic approaches
bass_notes = []
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    root = pretty_midi.note_number_to_name(53)  # F
    fifth = pretty_midi.note_number_to_name(58)  # C
    chromatic_approach_down = pretty_midi.note_number_to_name(52)  # E
    chromatic_approach_up = pretty_midi.note_number_to_name(59)  # D

    # Walking bass line: root, chromatic down, fifth, chromatic up
    for i, note in enumerate([53, 52, 58, 59]):
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

bass.notes.extend(bass_notes)

# Piano (Diane): open voicings, different chord each bar, resolve on the last
piano_notes = []
chords = [
    # Bar 2: Fm7
    [53, 57, 60, 64],
    # Bar 3: Bb7
    [50, 54, 57, 62],
    # Bar 4: Eb7
    [48, 52, 55, 59],
]

for bar in range(2, 5):
    start = (bar - 1) * 1.5
    chord = chords[bar - 2]
    for note in chord:
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.75))

piano.notes.extend(piano_notes)

# Sax (Dante): one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = []
# Bar 2: Start of motif
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.5 + 0.1875))  # G
sax_notes.append(pretty_midi.Note(velocity=110, pitch=60, start=1.5 + 0.375, end=1.5 + 0.375 + 0.1875))  # E
sax_notes.append(pretty_midi.Note(velocity=110, pitch=58, start=1.5 + 0.75, end=1.5 + 0.75 + 0.1875))  # D
# Bar 3: Leave it hanging
# No notes here, just silence
# Bar 4: Come back and finish
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.5 + 0.1875))  # G
sax_notes.append(pretty_midi.Note(velocity=110, pitch=64, start=4.5 + 0.375, end=4.5 + 0.375 + 0.1875))  # A
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5 + 0.75, end=4.5 + 0.75 + 0.1875))  # G

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
