
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
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5), (40, 1.875), (39, 2.25), (43, 2.625),
    (43, 2.625), (45, 3.0), (44, 3.375), (48, 3.75),
    (48, 3.75), (50, 4.125), (49, 4.5), (53, 4.875)
]
for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes_bar2 = [(62, 1.5), (67, 1.5), (69, 1.5), (64, 1.5)]
# Bar 3: Gm7 (G, Bb, D, F)
piano_notes_bar3 = [(67, 3.0), (71, 3.0), (69, 3.0), (65, 3.0)]
# Bar 4: Cmaj7 (C, E, G, B)
piano_notes_bar4 = [(60, 4.5), (64, 4.5), (67, 4.5), (71, 4.5)]
for chord in [piano_notes_bar2, piano_notes_bar3, piano_notes_bar4]:
    for note, time in zip(chord, [1.5, 1.875, 2.25, 2.625]):
        piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
        piano.notes.append(piano_note)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F# (67), G (67), D (62), leave it hanging on the next bar, then return with a variation
sax_notes = [
    (62, 1.5), (67, 1.875), (67, 2.25), (62, 2.625),
    (62, 4.5), (67, 4.875)
]
for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
