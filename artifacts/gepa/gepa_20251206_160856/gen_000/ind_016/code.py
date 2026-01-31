
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.375), (42, 0.75), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.875), (42, 2.25), (42, 2.625)
]

for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5), (40, 1.875), (38, 2.25), (41, 2.625),
    (43, 3.0), (41, 3.375), (40, 3.75), (38, 4.125),
    (43, 4.5), (41, 4.875), (43, 5.25), (45, 5.625)
]

for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes_bar2 = [50, 53, 57, 61]
# Bar 3: Gm7 (G, Bb, D, F)
piano_notes_bar3 = [55, 57, 62, 65]
# Bar 4: Cmaj7 (C, E, G, B)
piano_notes_bar4 = [60, 64, 67, 71]

for note in piano_notes_bar2:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=1.5, end=1.5 + 0.75)
    piano.notes.append(piano_note)

for note in piano_notes_bar3:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=3.0, end=3.0 + 0.75)
    piano.notes.append(piano_note)

for note in piano_notes_bar4:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=4.5, end=4.5 + 0.75)
    piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62), F# (64), B (67), D (62) - then rest for 0.75s, then back in with B (67), D (62)

sax_notes = [
    (62, 1.5), (64, 1.875), (67, 2.25), (62, 2.625),
    (67, 4.5), (62, 4.875)
]

for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 3.0), (38, 3.375), (42, 3.0), (42, 3.375), (42, 3.75), (42, 4.125),
    # Bar 3
    (36, 4.5), (38, 4.875), (42, 4.5), (42, 4.875), (42, 5.25), (42, 5.625)
]

for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
