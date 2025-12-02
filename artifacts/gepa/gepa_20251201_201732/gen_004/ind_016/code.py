
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
for i in range(4):  # 4 beats per bar
    time = i * 0.375
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375))  # Kick on 1 and 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.75))  # Snare on 2 and 4
    for j in range(2):  # Hihat on every 8th note
        hihat_time = time + j * 0.1875
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.1875))
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = []
# Bar 2: D (MIDI 38) -> F# (MIDI 41) -> G (MIDI 43) -> A (MIDI 45)
bass_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0))
# Bar 3: G (MIDI 43) -> A (MIDI 45) -> B (MIDI 47) -> D (MIDI 38)
bass_notes.append(pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=47, start=3.75, end=4.125))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5))
# Bar 4: D (MIDI 38) -> E (MIDI 40) -> F# (MIDI 41) -> G (MIDI 43)
bass_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0))
bass.notes.extend(bass_notes)

# Piano: Diane, open voicings, different chord each bar, resolve on the last
# Bar 2: G7 (D, F#, G, B)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=3.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # B4
]
# Bar 3: Cmaj7 (C, E, G, B)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5))
piano_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5))
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5))
piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5))
# Bar 4: A7 (A, C#, E, G)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0))
piano_notes.append(pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=6.0))
piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0))
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0))
piano.notes.extend(piano_notes)

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (MIDI 62), F# (MIDI 66), G (MIDI 67)
# Bar 2: Play first two notes, leave the third hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # leave hanging
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),  # come back and finish
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=66, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0)
]
sax.notes.extend(sax_notes)

# Drums: continue with same pattern for bars 2-4
for i in range(4):  # 4 beats per bar
    time = 1.5 + i * 0.375
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375))  # Kick on 1 and 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.75))  # Snare on 2 and 4
    for j in range(2):  # Hihat on every 8th note
        hihat_time = time + j * 0.1875
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.1875))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
