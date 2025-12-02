
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
#Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.75, 0.375),
    (36, 1.125, 0.375), (38, 1.5, 0.375)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Bass (D2-G2), roots and fifths with chromatic approaches
# D2 (D), F#2 (fifth), E2 (chromatic), G2 (fifth), F#2 (chromatic)
bass_notes = [
    (38, 1.5, 0.375), (41, 1.5, 0.375), (40, 1.5, 0.375),
    (43, 1.5, 0.375), (41, 1.5, 0.375), (40, 1.5, 0.375),
    (38, 1.5, 0.375), (41, 1.5, 0.375)
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano: Open voicings, different chord each bar
# Bar 2: Dmaj7 (D F# A C#)
pn = pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875)
piano.notes.append(pn)
pn = pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875)
piano.notes.append(pn)
pn = pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875)
piano.notes.append(pn)
pn = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875)
piano.notes.append(pn)

# Bar 3: D7 (D F# A C)
pn = pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625)
piano.notes.append(pn)
pn = pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625)
piano.notes.append(pn)
pn = pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625)
piano.notes.append(pn)
pn = pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.625)
piano.notes.append(pn)

# Bar 4: Dm7 (D F A C)
pn = pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375)
piano.notes.append(pn)
pn = pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375)
piano.notes.append(pn)
pn = pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375)
piano.notes.append(pn)
pn = pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375)
piano.notes.append(pn)

# Sax: Short motif, start on beat 1, leave it hanging
# Melody: D (50) - F# (53) - A (57) - D (50)
# Start on bar 2 (1.5s)
sax_notes = [
    (50, 1.5, 0.375), (53, 1.875, 0.375), (57, 2.25, 0.375), (50, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Drums continue for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start_time = 1.5 + (bar - 2) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.75, end=start_time + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.375, end=start_time + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.125, end=start_time + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start_time, end=start_time + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.375, end=start_time + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.75, end=start_time + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.125, end=start_time + 1.5)
    # Add to drums
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bass for bars 2-4
# Walking line with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375), (41, 1.5, 0.375), (40, 1.5, 0.375),
    (43, 1.5, 0.375), (41, 1.5, 0.375), (40, 1.5, 0.375),
    (38, 1.5, 0.375), (41, 1.5, 0.375),

    (38, 2.25, 0.375), (41, 2.25, 0.375), (40, 2.25, 0.375),
    (43, 2.25, 0.375), (41, 2.25, 0.375), (40, 2.25, 0.375),
    (38, 2.25, 0.375), (41, 2.25, 0.375),

    (38, 3.0, 0.375), (41, 3.0, 0.375), (40, 3.0, 0.375),
    (43, 3.0, 0.375), (41, 3.0, 0.375), (40, 3.0, 0.375),
    (38, 3.0, 0.375), (41, 3.0, 0.375)
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
