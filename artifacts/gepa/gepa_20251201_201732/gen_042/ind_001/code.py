
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

kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42, 42, 42, 42]

for i in range(2):
    kick = pretty_midi.Note(velocity=100, pitch=kick_notes[i], start=0.375 * i, end=0.375 * (i + 1))
    drums.notes.append(kick)
    snare = pretty_midi.Note(velocity=100, pitch=snare_notes[i], start=0.375 * (i + 1), end=0.375 * (i + 2))
    drums.notes.append(snare)
    for j in range(2):
        hihat = pretty_midi.Note(velocity=80, pitch=hihat_notes[j], start=0.375 * (i * 2 + j), end=0.375 * (i * 2 + j + 1))
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: D2-G2, roots and fifths with chromatic approaches (D2, F#2, G2, A2, Bb2, B2, C#3, D3, etc.)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25), # F#2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),  # A2
    pretty_midi.Note(velocity=90, pitch=44, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.75), # B2
    pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=4.125), # C#3
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),  # D3
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.875),  # E3
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25), # D3
    pretty_midi.Note(velocity=90, pitch=48, start=5.25, end=5.625), # C#3
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last beat of each bar
# Bar 2: Cmaj7 (C, E, G, B)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
]

# Bar 3: Dm7 (D, F, A, C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),
])

# Bar 4: G7 (G, B, D, F#)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),
])

# Bar 4: Resolve to Cmaj7 (C, E, G, B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),
])

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Motif: D - F# - G - A (Dorian)
# D (62), F# (66), G (67), A (69)
# Play the first two notes, then leave it hanging on A for the third bar, then return to finish the motif in the last bar

note1 = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.25)
note3 = pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625)
note4 = pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0)
note5 = pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375)
note6 = pretty_midi.Note(velocity=110, pitch=66, start=3.375, end=3.75)
note7 = pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125)
note8 = pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5)

sax.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8])

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

kick_times = [1.5, 2.25, 2.625, 3.375, 4.125, 4.875]
snare_times = [1.875, 2.625, 3.0, 3.75, 4.5, 5.25]
hihat_times = [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]

for t in kick_times:
    kick = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.375)
    drums.notes.append(kick)

for t in snare_times:
    snare = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.375)
    drums.notes.append(snare)

for t in hihat_times:
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.375)
    drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
