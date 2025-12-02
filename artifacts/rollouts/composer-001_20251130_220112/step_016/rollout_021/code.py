
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
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    dr_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm, chromatic approaches
bass_notes = [
    (46, 1.5), (47, 1.75), (45, 2.0), (44, 2.25),  # Fm root motion
    (46, 2.5), (47, 2.75), (45, 3.0), (44, 3.25),
    (46, 3.5), (47, 3.75), (45, 4.0), (44, 4.25),
    (46, 4.5), (47, 4.75), (45, 5.0), (44, 5.25)
]
for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (53, 1.75), (50, 1.75), (48, 1.75), (43, 1.75),  # F7
    # Bar 3
    (55, 2.75), (52, 2.75), (50, 2.75), (46, 2.75),  # Bb7
    # Bar 4
    (53, 3.75), (50, 3.75), (48, 3.75), (43, 3.75)   # F7 again
]
for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Drums continue: same pattern
for i in range(2, 5):
    for note, offset in [(36, 0.0), (38, 0.375), (42, 0.375),
                         (36, 0.75), (38, 1.125), (42, 1.125)]:
        dr_note = pretty_midi.Note(velocity=100, pitch=note, start=1.5 + (i - 1) * 1.5 + offset, end=1.5 + (i - 1) * 1.5 + offset + 0.125)
        drums.notes.append(dr_note)

# Sax: One short motif, make it sing
# Start on F (46), move to Ab (48), then G (47), ending on F (46)
sax_notes = [
    (46, 1.5), (48, 1.75), (47, 2.0), (46, 2.25),
    (46, 2.5), (48, 2.75), (47, 3.0), (46, 3.25),
    (46, 3.5), (48, 3.75), (47, 4.0), (46, 4.25),
    (46, 4.5), (48, 4.75), (47, 5.0), (46, 5.25)
]
for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dantes_intro.mid")
