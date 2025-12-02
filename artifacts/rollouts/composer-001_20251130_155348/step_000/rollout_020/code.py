
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (0.0, 36),  # Kick on 1
    (0.75, 42), # Hihat on &1
    (1.0, 38),  # Snare on 2
    (1.5, 36)   # Kick on 3
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches, never same note twice
bass_notes = [
    (1.5, 46), (1.75, 47), (2.0, 48), (2.25, 49),
    (2.5, 49), (2.75, 50), (3.0, 51), (3.25, 52),
    (3.5, 52), (3.75, 51), (4.0, 50), (4.25, 49),
    (4.5, 48), (4.75, 47), (5.0, 46), (5.25, 45)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    (2.0, 62), (2.0, 67), (2.0, 71), (2.0, 74),  # D7 on 2
    (3.0, 62), (3.0, 67), (3.0, 71), (3.0, 74),  # D7 on 4
    (4.0, 62), (4.0, 67), (4.0, 71), (4.0, 74)   # D7 on 4
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.25))

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    bar_start = 1.5 * (bar - 1)
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.25)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.0)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.5, end=bar_start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.25, end=bar_start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start, end=bar_start + 0.25)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.25, end=bar_start + 0.5)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.5, end=bar_start + 0.75)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.75, end=bar_start + 1.0)
    hihat5 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.0, end=bar_start + 1.25)
    hihat6 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.25, end=bar_start + 1.5)
    # Add all notes
    drums.notes.append(kick1)
    drums.notes.append(kick3)
    drums.notes.append(snare2)
    drums.notes.append(snare4)
    drums.notes.append(hihat1)
    drums.notes.append(hihat2)
    drums.notes.append(hihat3)
    drums.notes.append(hihat4)
    drums.notes.append(hihat5)
    drums.notes.append(hihat6)

# Dante on tenor: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F7 - G7 - A7 - B7 (in 16th notes)
sax_notes = [
    (1.5, 66), (1.575, 67), (1.65, 69), (1.725, 71),
    (2.5, 66), (2.575, 67), (2.65, 69), (2.725, 71),
    (3.5, 66), (3.575, 67), (3.65, 69), (3.725, 71)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.075))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI
midi.write('dante_intro.mid')
