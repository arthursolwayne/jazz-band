
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
    # Bar 1
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.1875), (42, 0.375), (42, 0.5625),
    (42, 0.75), (42, 0.9375), (42, 1.125), (42, 1.3125), (36, 1.5),
    (38, 1.875), (42, 1.5), (42, 1.6875), (42, 1.875), (42, 2.0625),
    (42, 2.25), (42, 2.4375), (42, 2.625), (42, 2.8125), (42, 3.0)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm (F, Eb, D, C), chromatic approaches
bass_notes = [
    # Bar 2
    (64, 1.5), (63, 1.875), (62, 2.25), (60, 2.625),
    # Bar 3
    (64, 3.0), (62, 3.375), (61, 3.75), (59, 4.125),
    # Bar 4
    (64, 4.5), (63, 4.875), (62, 5.25), (60, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (53, 1.875), (57, 1.875), (55, 1.875), (50, 1.875),
    (53, 2.625), (57, 2.625), (55, 2.625), (50, 2.625),
    # Bar 3
    (53, 3.375), (57, 3.375), (55, 3.375), (50, 3.375),
    (53, 4.125), (57, 4.125), (55, 4.125), (50, 4.125),
    # Bar 4
    (53, 4.875), (57, 4.875), (55, 4.875), (50, 4.875),
    (53, 5.625), (57, 5.625), (55, 5.625), (50, 5.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.25))

# Sax: Short motif, start it, leave it hanging, come back and finish it
# Fm motif: F - Ab - Bb - G (Fm7)
sax_notes = [
    (64, 1.5), (62, 1.6875), (62, 1.875), (67, 2.0625),
    # Leave it hanging
    (62, 2.25), (62, 2.4375), (62, 2.625), (62, 2.8125),
    # Come back and finish it
    (64, 3.0), (62, 3.1875), (62, 3.375), (67, 3.5625),
    # Carry it through
    (64, 3.75), (62, 3.9375), (62, 4.125), (67, 4.3125),
    (64, 4.5), (62, 4.6875), (62, 4.875), (67, 5.0625),
    (64, 5.25), (62, 5.4375), (62, 5.625), (67, 5.8125)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Drums: continue in bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick
    kick = pretty_midi.Note(velocity=90, pitch=36, start=bar_start, end=bar_start + 0.125)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=90, pitch=36, start=bar_start + 0.75, end=bar_start + 0.875)
    drums.notes.append(kick)
    # Snare
    snare = pretty_midi.Note(velocity=90, pitch=38, start=bar_start + 0.375, end=bar_start + 0.4375)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=90, pitch=38, start=bar_start + 1.125, end=bar_start + 1.1875)
    drums.notes.append(snare)
    # Hihat
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=bar_start, end=bar_start + 0.125)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.1875, end=bar_start + 0.3125)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.375, end=bar_start + 0.5)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.5625, end=bar_start + 0.6875)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.75, end=bar_start + 0.875)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.9375, end=bar_start + 1.0625)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 1.125, end=bar_start + 1.25)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 1.3125, end=bar_start + 1.4375)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 1.5, end=bar_start + 1.625)
    drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write("dante_intro.mid")
