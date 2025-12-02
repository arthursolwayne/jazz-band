
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
    (36, 0.0, 0.5),     # Kick on 1
    (42, 0.375, 0.25),  # Hi-hat on &1
    (38, 0.75, 0.5),    # Snare on 2
    (42, 1.125, 0.25),  # Hi-hat on &3
    (36, 1.5, 0.5),     # Kick on 3
    (42, 1.875, 0.25),  # Hi-hat on &4
]

for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),   # Dm7: D
    (63, 1.875, 0.375), # Eb
    (62, 2.25, 0.375),  # D
    (60, 2.625, 0.375), # Bb
    (62, 3.0, 0.375),   # D
    (63, 3.375, 0.375), # Eb
    (62, 3.75, 0.375),  # D
    (60, 4.125, 0.375), # Bb
    (62, 4.5, 0.375),   # D
    (63, 4.875, 0.375), # Eb
    (62, 5.25, 0.375),  # D
    (60, 5.625, 0.375), # Bb
]

for note, start, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# Piano: Diane, 7th chords, comp on 2 and 4
piano_notes = [
    (62, 2.25, 0.375),  # D7: D
    (64, 2.25, 0.375),  # F
    (67, 2.25, 0.375),  # A
    (69, 2.25, 0.375),  # C
    (62, 3.75, 0.375),  # D
    (64, 3.75, 0.375),  # F
    (67, 3.75, 0.375),  # A
    (69, 3.75, 0.375),  # C
    (62, 5.25, 0.375),  # D
    (64, 5.25, 0.375),  # F
    (67, 5.25, 0.375),  # A
    (69, 5.25, 0.375),  # C
]

for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Drums: Bars 2-4
drum_notes = [
    (36, 1.5, 0.5),     # Kick on 1
    (42, 1.875, 0.25),  # Hi-hat on &1
    (38, 2.25, 0.5),    # Snare on 2
    (42, 2.625, 0.25),  # Hi-hat on &3
    (36, 3.0, 0.5),     # Kick on 3
    (42, 3.375, 0.25),  # Hi-hat on &4
    (36, 3.75, 0.5),    # Kick on 1
    (42, 4.125, 0.25),  # Hi-hat on &1
    (38, 4.5, 0.5),     # Snare on 2
    (42, 4.875, 0.25),  # Hi-hat on &3
    (36, 5.25, 0.5),    # Kick on 3
    (42, 5.625, 0.25),  # Hi-hat on &4
]

for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Sax: Dante, motif in Dm, one short phrase, ends on a question
sax_notes = [
    (62, 1.5, 0.375),   # D (start)
    (64, 1.875, 0.375), # F
    (60, 2.25, 0.375),  # Bb
    (62, 2.625, 0.375), # D
    (64, 3.0, 0.375),   # F
    (60, 3.375, 0.375), # Bb
    (62, 3.75, 0.375),  # D
    (64, 4.125, 0.375), # F
    (60, 4.5, 0.375),   # Bb
    (62, 4.875, 0.375), # D (end, unfinished)
]

for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
