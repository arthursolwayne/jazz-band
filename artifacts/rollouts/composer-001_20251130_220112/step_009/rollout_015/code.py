
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
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (36, 1.5), (37, 1.75), (38, 2.0), (39, 2.25),  # F7 chord
    (40, 2.5), (41, 2.75), (42, 3.0), (43, 3.25),  # B7 chord
    (36, 3.5), (37, 3.75), (38, 4.0), (39, 4.25),  # F7 chord
    (40, 4.5), (41, 4.75), (42, 5.0), (43, 5.25)   # B7 chord
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (48, 1.75), (50, 1.75), (53, 1.75),  # F7
    (60, 2.25), (62, 2.25), (65, 2.25),  # B7
    # Bar 3
    (48, 3.25), (50, 3.25), (53, 3.25),  # F7
    (60, 3.75), (62, 3.75), (65, 3.75),  # B7
    # Bar 4
    (48, 4.75), (50, 4.75), (53, 4.75),  # F7
    (60, 5.25), (62, 5.25), (65, 5.25)   # B7
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Sax: Motif in F, short, singable, leave it hanging
# F (48), A (50), B (52), F (48) - then repeat with slight variation
sax_notes = [
    (48, 1.5), (50, 1.75), (52, 2.0), (48, 2.25),
    (48, 2.5), (50, 2.75), (52, 3.0), (48, 3.25),
    (48, 3.5), (50, 3.75), (52, 4.0), (48, 4.25),
    (48, 4.5), (50, 4.75), (52, 5.0), (48, 5.25)
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
