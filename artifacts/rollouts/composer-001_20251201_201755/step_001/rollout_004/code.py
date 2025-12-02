
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.375),
    (42, 0.75), (42, 1.125), (36, 1.5),
    (38, 1.875), (42, 1.5), (42, 1.875),
    (42, 2.25), (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with roots and fifths, chromatic approaches
bass_notes = [
    (38, 1.5), (40, 1.875), (37, 2.25), (40, 2.625),
    (43, 3.0), (45, 3.375), (42, 3.75), (45, 4.125),
    (47, 4.5), (49, 4.875), (46, 5.25), (49, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    (62, 1.5), (67, 1.5), (69, 1.5), (72, 1.5),
    # Bar 3: D7 (D-F#-A-C)
    (62, 3.0), (67, 3.0), (69, 3.0), (71, 3.0),
    # Bar 4: Dm7 (D-F-A-C)
    (62, 4.5), (66, 4.5), (69, 4.5), (72, 4.5),
    # Resolutions
    (62, 6.0), (67, 6.0), (69, 6.0), (72, 6.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D - F# - B - D (first bar, ends on D)
sax_notes = [
    (62, 1.5), (67, 1.875), (71, 2.25), (62, 2.625),
    # Leave it hanging (no note here)
    # Come back and finish it
    (67, 4.5), (71, 4.875), (62, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_introduction.mid')
