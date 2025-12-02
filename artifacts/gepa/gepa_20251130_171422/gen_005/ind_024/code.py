
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm (F, Eb, D, C, Bb, B, A, Ab)
bass_notes = [
    (53, 1.5), (51, 1.875), (50, 2.25), (48, 2.625),
    (53, 3.0), (54, 3.375), (52, 3.75), (51, 4.125),
    (53, 4.5), (51, 4.875), (50, 5.25), (48, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Diane: 7th chords on 2 and 4, comp in Fm
piano_notes = [
    # Bar 2: F7 on 2, Bb7 on 4
    (53, 3.375), (50, 3.375), (48, 3.375), (45, 3.375),  # F7
    (55, 4.125), (52, 4.125), (49, 4.125), (46, 4.125),  # Bb7
    # Bar 3: F7 on 2, Bb7 on 4
    (53, 4.875), (50, 4.875), (48, 4.875), (45, 4.875),
    (55, 5.625), (52, 5.625), (49, 5.625), (46, 5.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Dante: Sax line - one short motif, make it sing
# Fm motif: F (53), Ab (50), Bb (48), Eb (51) - starting on 1.5s
sax_notes = [
    (53, 1.5), (50, 1.75), (48, 2.0), (51, 2.25),  # First phrase
    (53, 2.5), (50, 2.75), (48, 3.0), (51, 3.25),  # Second phrase
    (53, 3.5), (50, 3.75), (48, 4.0), (51, 4.25),  # Third phrase
    (53, 4.5), (50, 4.75), (48, 5.0), (51, 5.25)   # Final phrase
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: Bars 2-4
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
