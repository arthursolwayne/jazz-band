
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
bar_length = 1.5
for i in range(4):
    time = i * bar_length / 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + bar_length / 4))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + bar_length / 4, end=time + bar_length / 2))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + bar_length, step=bar_length / 8))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + bar_length / 4),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=1.5 + bar_length / 4, end=1.5 + bar_length / 2),  # Gb
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + bar_length / 2, end=1.5 + 3 * bar_length / 4),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 3 * bar_length / 4, end=1.5 + bar_length),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.5 + bar_length, end=1.5 + bar_length + bar_length / 4),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=1.5 + bar_length + bar_length / 4, end=1.5 + bar_length + bar_length / 2),  # C#
    pretty_midi.Note(velocity=100, pitch=74, start=1.5 + bar_length + bar_length / 2, end=1.5 + bar_length + 3 * bar_length / 4),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=1.5 + bar_length + 3 * bar_length / 4, end=1.5 + 2 * bar_length),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 2 * bar_length, end=1.5 + 2 * bar_length + bar_length / 4),
    pretty_midi.Note(velocity=100, pitch=65, start=1.5 + 2 * bar_length + bar_length / 4, end=1.5 + 2 * bar_length + bar_length / 2),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 2 * bar_length + bar_length / 2, end=1.5 + 2 * bar_length + 3 * bar_length / 4),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 2 * bar_length + 3 * bar_length / 4, end=1.5 + 3 * bar_length),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# F7, Bb7, F7, Bb7
chords = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + bar_length / 2),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.5 + bar_length / 2),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + bar_length / 2),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.5 + bar_length / 2),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.5 + bar_length, end=1.5 + 3 * bar_length / 2),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + bar_length, end=1.5 + 3 * bar_length / 2),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.5 + bar_length, end=1.5 + 3 * bar_length / 2),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=1.5 + bar_length, end=1.5 + 3 * bar_length / 2),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 2 * bar_length, end=1.5 + 5 * bar_length / 2),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 2 * bar_length, end=1.5 + 5 * bar_length / 2),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 2 * bar_length, end=1.5 + 5 * bar_length / 2),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=1.5 + 2 * bar_length, end=1.5 + 5 * bar_length / 2),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 3 * bar_length, end=1.5 + 7 * bar_length / 2),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 3 * bar_length, end=1.5 + 7 * bar_length / 2),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 3 * bar_length, end=1.5 + 7 * bar_length / 2),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=1.5 + 3 * bar_length, end=1.5 + 7 * bar_length / 2),  # D
]
piano.notes.extend(chords)

# Sax: Motif, start it, leave it hanging, come back and finish it
# Fm7 -> Ab -> Bb -> F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + bar_length / 4),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + bar_length / 4, end=1.5 + bar_length / 2),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + bar_length / 2, end=1.5 + 3 * bar_length / 4),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 3 * bar_length / 4, end=1.5 + bar_length),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5 + bar_length, end=1.5 + bar_length + bar_length / 4),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + bar_length + bar_length / 4, end=1.5 + bar_length + bar_length / 2),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + bar_length + bar_length / 2, end=1.5 + bar_length + 3 * bar_length / 4),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5 + bar_length + 3 * bar_length / 4, end=1.5 + 2 * bar_length),
]
sax.notes.extend(sax_notes)

# Drums: Continue for bars 2-4
for i in range(4, 8):
    time = i * bar_length / 4 + 1.5
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + bar_length / 4))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + bar_length / 4, end=time + bar_length / 2))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + bar_length, step=bar_length / 8))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
