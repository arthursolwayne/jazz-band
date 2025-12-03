
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
kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875, 5.625]
hihat_times = [i * 0.375 for i in range(0, 16)]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.05)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.75),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=1.75, end=2.0),  # F#2
    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.25),  # A2
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.5),  # G2
    pretty_midi.Note(velocity=80, pitch=38, start=2.5, end=2.75),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=2.75, end=3.0),  # F#2
]

bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
diane_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),  # C#4
]

piano.notes.extend(diane_notes)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62), F#4 (67), A4 (71), D5 (72) - start on 1.5, end on 2.0 (first 2 notes), then 3.0-3.5 (finish)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=2.0),
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.5),
    pretty_midi.Note(velocity=110, pitch=71, start=2.5, end=3.0),
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.5),
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=4.0),
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.5)
]

sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.25),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=3.25, end=3.5),  # F#2
    pretty_midi.Note(velocity=80, pitch=43, start=3.5, end=3.75),  # A2
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.0),  # G2
    pretty_midi.Note(velocity=80, pitch=38, start=4.0, end=4.25),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=4.25, end=4.5),  # F#2
]

bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: G7 (G, B, D, F#)
diane_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=4.5),  # F#4
]

piano.notes.extend(diane_notes)

# Dante: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.5),
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=4.0),
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.5)
]

sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.75),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=4.75, end=5.0),  # F#2
    pretty_midi.Note(velocity=80, pitch=43, start=5.0, end=5.25),  # A2
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.5),  # G2
    pretty_midi.Note(velocity=80, pitch=38, start=5.5, end=5.75),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=5.75, end=6.0),  # F#2
]

bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: C7 (C, E, G, B)
diane_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=6.0),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=6.0),  # B4
]

piano.notes.extend(diane_notes)

# Dante: Finish motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=5.0),
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.5),
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=6.0)
]

sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
kick_times = [3.0, 3.75, 4.5, 5.25]
snare_times = [3.375, 4.125, 4.875, 5.625]
hihat_times = [i * 0.375 for i in range(16, 32)]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.05)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
