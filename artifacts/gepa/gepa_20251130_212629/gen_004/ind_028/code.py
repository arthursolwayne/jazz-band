
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

# Bass line: walking line in Fm, chromatic approaches
bass_notes = [
    (39, 1.5), (40, 1.875), (38, 2.25), (37, 2.625),
    (39, 3.0), (40, 3.375), (38, 3.75), (37, 4.125),
    (39, 4.5), (40, 4.875), (38, 5.25), (37, 5.625)
]
for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4, comping in Fm
piano_notes = [
    # Bar 2: F7 on 2 and 4
    (53, 3.0), (50, 3.0), (48, 3.0), (51, 3.0),
    (53, 3.375), (50, 3.375), (48, 3.375), (51, 3.375),
    # Bar 3: Bbm7 on 2 and 4
    (57, 4.5), (52, 4.5), (49, 4.5), (50, 4.5),
    (57, 4.875), (52, 4.875), (49, 4.875), (50, 4.875),
    # Bar 4: Dm7 on 2 and 4
    (58, 6.0), (54, 6.0), (50, 6.0), (52, 6.0),
    (58, 6.375), (54, 6.375), (50, 6.375), (52, 6.375)
]
for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(piano_note)

# Sax: Motif in Fm, one short phrase, leave it hanging
sax_notes = [
    (53, 1.5), (51, 1.875), (48, 2.25), (50, 2.625),
    (53, 3.0), (51, 3.375), (48, 3.75), (50, 4.125),
    (53, 4.5), (51, 4.875), (48, 5.25), (50, 5.625)
]
for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

# Add more fills and energy from Little Ray in bars 2-4
drum_fills = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_fills:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("fm_jazz_intro.mid")
