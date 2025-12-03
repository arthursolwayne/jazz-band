
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
drum_notes = [
    # Bar 1
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.75), (42, 0.375, 0.75),
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.125, 0.75), (42, 1.5, 0.75),
]

for note_number, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    (64, 1.5, 0.375), (65, 1.875, 0.375), (64, 2.25, 0.375), (65, 2.625, 0.375),
    # Bar 3
    (67, 3.0, 0.375), (68, 3.375, 0.375), (67, 3.75, 0.375), (68, 4.125, 0.375),
    # Bar 4
    (64, 4.5, 0.375), (65, 4.875, 0.375), (64, 5.25, 0.375), (65, 5.625, 0.375),
]

for note_number, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_number, start=start, end=start + duration)
    bass.notes.append(note)

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7
piano_notes = [
    # Bar 2
    (64, 1.5, 0.375), (67, 1.5, 0.375), (71, 1.5, 0.375), (76, 1.5, 0.375),
    # Bar 3: Bb7
    (69, 3.0, 0.375), (72, 3.0, 0.375), (76, 3.0, 0.375), (81, 3.0, 0.375),
    # Bar 4: Cm7
    (60, 4.5, 0.375), (63, 4.5, 0.375), (67, 4.5, 0.375), (72, 4.5, 0.375),
]

for note_number, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    piano.notes.append(note)

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.75), (42, 1.875, 0.75),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.75), (42, 2.625, 0.75),
    # Bar 3
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.75), (42, 3.375, 0.75),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.75), (42, 4.125, 0.75),
    # Bar 4
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.75), (42, 4.875, 0.75),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.75), (42, 5.625, 0.75),
]

for note_number, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

# Dante on sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    (66, 1.5, 0.375), (67, 1.875, 0.375), (66, 2.25, 0.375),
    # Leave it hanging — rest until Bar 4
    # Bar 4: Come back and finish the motif
    (66, 4.5, 0.375), (67, 4.875, 0.375), (66, 5.25, 0.375),
]

for note_number, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=note_number, start=start, end=start + duration)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
