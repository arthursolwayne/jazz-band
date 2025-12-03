
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
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125, 
               1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125, 
               3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125, 
               4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

# Add the drum notes
for time in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
    drums.notes.append(note)

for time in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
    drums.notes.append(note)

for time in hihat_times:
    note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in D (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.75),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.75, end=2.0),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.25),  # A2
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.5),  # G2
    pretty_midi.Note(velocity=90, pitch=38, start=2.5, end=2.75),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=2.75, end=3.0),  # F2
]

bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C#)
diane_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # C#5
]

# Bar 3: G7 (G B D F)
diane_notes += [
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.25),  # F5
]

# Bar 4: A7 (A C# E G)
diane_notes += [
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # C#5
    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=2.75),  # E5
    pretty_midi.Note(velocity=100, pitch=77, start=2.5, end=2.75),  # G5
]

piano.notes.extend(diane_notes)

# Dante: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62) -> F# (67) -> A (72) -> C# (74)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75),  # F#4
    pretty_midi.Note(velocity=110, pitch=72, start=1.75, end=1.875),  # A4
    pretty_midi.Note(velocity=110, pitch=74, start=1.875, end=2.0),  # C#5
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.125),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=3.125, end=3.25),  # F#4
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.375),  # D4
]

sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # G2
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),  # Bb2
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),  # D3
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.0),  # C3
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.25),  # G2
    pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5),  # Bb2
]

bass.notes.extend(bass_notes)

# Diane: Open voicings
diane_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.25),  # F5

    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # C#5
    pretty_midi.Note(velocity=100, pitch=74, start=3.5, end=3.75),  # E5
    pretty_midi.Note(velocity=100, pitch=77, start=3.5, end=3.75),  # G5
]

piano.notes.extend(diane_notes)

# Dante: Continuation of motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=74, start=3.0, end=3.125),  # C#5
    pretty_midi.Note(velocity=110, pitch=72, start=3.125, end=3.25),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.375),  # F#4
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5),  # D4
]

sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # D3
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),  # E3
    pretty_midi.Note(velocity=90, pitch=72, start=5.0, end=5.25),  # G3
    pretty_midi.Note(velocity=90, pitch=70, start=5.25, end=5.5),  # F3
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.75),  # D3
    pretty_midi.Note(velocity=90, pitch=69, start=5.75, end=6.0),  # E3
]

bass.notes.extend(bass_notes)

# Diane: Open voicings
diane_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75),  # F5
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.75),  # G5

    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # C#5
    pretty_midi.Note(velocity=100, pitch=74, start=5.0, end=5.25),  # E5
    pretty_midi.Note(velocity=100, pitch=77, start=5.0, end=5.25),  # G5
]

piano.notes.extend(diane_notes)

# Dante: Completion of motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.625),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=4.625, end=4.75),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=4.875),  # F#4
    pretty_midi.Note(velocity=110, pitch=72, start=4.875, end=5.0),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.125),  # F#4
    pretty_midi.Note(velocity=110, pitch=62, start=5.125, end=5.25),  # D4
]

sax.notes.extend(sax_notes)

# Bar 4: Drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_times = [4.5, 5.25]
snare_times = [4.875, 5.625]
hihat_times = [4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

# Add the drum notes
for time in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
    drums.notes.append(note)

for time in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
    drums.notes.append(note)

for time in hihat_times:
    note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
