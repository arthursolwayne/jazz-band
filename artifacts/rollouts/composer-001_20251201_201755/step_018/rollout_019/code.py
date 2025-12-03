
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
drum_notes = []
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 2 and 4
    drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75))
    drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on every eighth
    for i in range(8):
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = []
for bar in range(2, 5):
    start = bar * 1.5
    # D2 (MIDI 38) in bar 2
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=38, start=start, end=start + 0.375))
    # F#2 (MIDI 41) in bar 2
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=41, start=start + 0.375, end=start + 0.75))
    # G2 (MIDI 43) in bar 2
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=43, start=start + 0.75, end=start + 1.125))
    # D2 (MIDI 38) in bar 2
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=38, start=start + 1.125, end=start + 1.5))

    # F#2 (MIDI 41) in bar 3
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=41, start=start + 0.375, end=start + 0.75))
    # G2 (MIDI 43) in bar 3
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=43, start=start + 0.75, end=start + 1.125))
    # A2 (MIDI 45) in bar 3
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=45, start=start + 1.125, end=start + 1.5))

    # G2 (MIDI 43) in bar 4
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=43, start=start, end=start + 0.375))
    # B2 (MIDI 46) in bar 4
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=46, start=start + 0.375, end=start + 0.75))
    # D3 (MIDI 49) in bar 4
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=49, start=start + 0.75, end=start + 1.125))
    # G2 (MIDI 43) in bar 4
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=43, start=start + 1.125, end=start + 1.5))

bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
piano_notes = []
for bar in range(2, 5):
    start = bar * 1.5
    # Bar 2: D7 (D, F#, A, C#)
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=62, start=start, end=start + 0.375))
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=start, end=start + 0.375))
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=start, end=start + 0.375))
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=76, start=start, end=start + 0.375))
    # Bar 3: G7 (G, B, D, F#)
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=start + 0.375, end=start + 0.75))
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=72, start=start + 0.375, end=start + 0.75))
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=76, start=start + 0.375, end=start + 0.75))
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=81, start=start + 0.375, end=start + 0.75))
    # Bar 4: C7 (C, E, G, B)
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=60, start=start + 0.75, end=start + 1.125))
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=65, start=start + 0.75, end=start + 1.125))
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=72, start=start + 0.75, end=start + 1.125))
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=77, start=start + 0.75, end=start + 1.125))
    # Resolve on the last bar (D7)
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=62, start=start + 1.125, end=start + 1.5))
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=start + 1.125, end=start + 1.5))
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=start + 1.125, end=start + 1.5))
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=76, start=start + 1.125, end=start + 1.5))

piano.notes.extend(piano_notes)

# You: Tenor sax — one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = []
start = 1.5
# Bar 2: Start the motif (E4, B4, D5)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=start, end=start + 0.375))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=start + 0.375, end=start + 0.75))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=72, start=start + 0.75, end=start + 1.125))

# Bar 3: Leave it hanging
sax_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=start + 1.125, end=start + 1.5))

# Bar 4: Come back and finish it (E4, B4, D5, E4)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=start + 1.5, end=start + 1.875))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=start + 1.875, end=start + 2.25))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=72, start=start + 2.25, end=start + 2.625))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=start + 2.625, end=start + 3.0))

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
